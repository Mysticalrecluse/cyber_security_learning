## Kubernetes Gateway API

 为了克服Ingress的不足之处，Kubernetes提出来Gateway API

实现了Gateway API的开源Kubernetes生态软件是 **Istio**



### Gateway API 介绍

**官方网站**

```http
https://gateway-api.sigs.k8s.io/
```

![image-20250320135332678](../markdown_img/image-20250320135332678.png)



如上图：Gateway API 把人员角色分为3类

1. **Infrastructure Provider**：基础设施提供者，主要负责GatewayClass，把Gateway Controller 和 Gateway 关联起来，负责整个底层设施的提供，给Gateway 提供 gatewayClassName
2. **Cluster Operator**：集群操作者，主要负责 Gateway，**类似反向代理的前端**
3. **Application Develops**：应用开发者，负责开发业务 Service，**类似反向代理的后端**



### Gateway API 流量分发流程

#### A Simple Gateway

![image-20250320141009871](../markdown_img/image-20250320141009871.png)

**1️⃣ 客户端请求**

客户端（例如浏览器或 API 调用）向某个域名或 IP 发起 HTTP/S 请求。

**2️⃣ 负载均衡（Gateway）**

**Gateway** 组件充当了整个系统的入口，通常对应一个 **Load Balancer**（负载均衡器）或者 Kubernetes 内部的 `Gateway` 资源。

- Gateway 的作用
  - 监听外部请求（通常是 HTTP 或 HTTPS）
  - 将匹配的流量转发给适当的 **HTTPRoute**
  - 可绑定多个 `HTTPRoute` 资源，处理不同路径的流量

**Gateway 配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: foo-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
    - protocol: HTTP
      port: 80
      name: http
      allowedRoutes:
        namespaces:
          from: All	
```

- **gatewayClassName: nginx** → 说明使用 Nginx Gateway Controller 处理流量

- **listeners.port: 80** → 监听 HTTP 80 端口

- **allowedRoutes** → 允许所有命名空间的 `HTTPRoute` 关联该 `Gateway`

**3️⃣ 路由匹配（HTTPRoute）**

**HTTPRoute** 负责定义流量的转发规则，例如：

- **路径匹配（Path Matching）**
- **主机匹配（Host Matching）**
- **流量权重（Traffic Splitting）**

**HTTPRoute 配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: foo-route
  namespace: default
spec:
  parentRefs:
    - name: foo-gateway  # 绑定 Gateway
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: "/"  # 匹配所有流量
      backendRefs:
        - name: foo-svc  # 指定 Service
          port: 80
```

- **`parentRefs: foo-gateway`** → 说明该 HTTPRoute 绑定到 `foo-gateway`
- **`matches: path: "/"`** → 说明匹配所有请求路径
- **`backendRefs: foo-svc`** → 指定流量转发到 `foo-svc` Service

**4️⃣ Service 发现**

Gateway 发现 `foo-svc` Service，并将流量转发给该 Service。

- Service 的作用
  - 负责负载均衡，将请求转发给 Pod
  - 通过 `selector` 选择匹配的 Pod

**Service 配置示例**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: foo-svc
  namespace: default
spec:
  selector:
    app: foo
  ports:
    - port: 80
      targetPort: 8080  # 转发到 Pod 的 8080 端口
```

- **selector: app=foo** → 选择标签为 `app=foo` 的 Pod
- **port: 80 → targetPort: 8080** → Service 监听 80 端口，但实际转发给 Pod 的 8080 端口

**5️⃣ 进入 Pod**

最终，流量会被路由到 **符合 `app=foo` 选择器的 Pod**，Pod 上的应用程序处理请求并返回响应。

```ABAP
注意：和Ingress相同，从 Gateway API 接收请求会直接发往后端 Pod，Service在这里用作服务发现
```



### Gateway 声明式实现

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: prod-web
spec:
  gatewayClassName: example    # 使用的GatewayClass是什么
  listeners:
  - protocol: HTTP
    port: 80
    name: prod-web-gw
    allowedRoutes:
      namespaces:
        from: Same        # 这里表明Gateway可以跨名称空间路由，但是Ingress不行
```



### HTTPRoute 声明式实现

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: foo
spec:
  parentRefs:
  - name: prod-web          # 关联指定的Gateway的Name
  rules:
  - backendRefs:
    - name: foo-svc
      port: 8080
```



#### HTTPRoute 官方示例

![image-20250320144558874](D:\git_repository\cyber_security_learning\markdown_img\image-20250320144558874.png)

##### 创建 Gateway 资源

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
spec:
  gatewayClassName: example-gateway-class
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: foo-route
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "foo.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /login
    backendRefs:
    - name: foo-svc
      port: 8080
      
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: bar-route
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "bar.example.com"
  rules:
  - matches:
    - headers:
      - type: Exact
        name: env
        value: canary
    backendRefs:
    - name: bar-svc-canary
      port: 8080
  - backendRefs:
    - name: bar-svc
      port: 8080
```



#### HTTP redirects and rewrites ( 重定向与重写 )

##### HTTP redirects Http -> Https

重定向会将 HTTP 3XX 响应返回给客户端，指示其检索其他资源。RequestRedirect 规则过滤器指示网关对与已过滤 HTTPRoute 规则匹配的请求发出重定向响应。

重定向过滤器可以独立替换各种 URL 组件。例如，要发出从 HTTP 到 HTTPS 的永久重定向 (301)，请配置`requestRedirect.statusCode=301` 和  `requestRedirect.scheme="https"`：

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-filter-redirect
spec:
  parentRefs:
  - name: redirect-gateway
    sectionName: http                    # 这里要匹配Gateway资源的listeners.name
  hostnames:
  - redirect.example
  rules:
  - filters:                             # 使用过滤器重定向
    - type: RequestRedirect              # 类型：请求重定向
      requestRedirect:
        scheme: https                    # 重定向到https
        statusCode: 301                  # 指定重定向状态码
```

因为上面的示例是从 http 重定向到 https，所以 Gateway 肯定要监听 https，下面是 Gateway 的示例

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: redirect-gateway
spec:
  gatewayClassName: foo-lb
  listeners:
  - name: http
    protocol: HTTP
    port: 80
  - name: https
    protocol: HTTPS
    port: 443
    tls:
      mode: Terminate
      certificateRefs:
      - name: redirect-example
```

###### tls.mode详解

在 **Gateway API** 的 `HTTPRoute` 或 `Gateway` 配置中，`tls.mode` 决定了 **TLS 终结方式**，即如何处理 HTTPS 流量。

**🔹 `tls.mode` 可选值**

| **值**        | **含义**                                                     |
| ------------- | ------------------------------------------------------------ |
| `Terminate`   | **终结 TLS（TLS Termination）**：Gateway 终结 TLS 连接并将流量解密后转发给后端（后端使用 HTTP） |
| `Passthrough` | **透传 TLS（TLS Passthrough）**：Gateway 不终结 TLS，直接将加密流量转发给后端（后端处理 TLS 证书） |
| `Mutual`      | **双向 TLS（mTLS，Mutual TLS）**：除了终结 TLS 外，还要求客户端提供证书进行双向认证 |

**示例：TLS 终结（TLS Termination）**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
    - protocol: HTTPS
      port: 443
      name: https
      tls:
        mode: Terminate  # 在 Gateway 终结 TLS
        certificateRefs:
          - name: example-tls-secret  # 这里是 Kubernetes Secret 名称
  addresses:
    - type: IPAddress
      value: 192.168.1.100
```

 **解释**

- **`tls.mode: Terminate`** → 说明 **TLS 由 Gateway 处理**
- **`certificateRefs.name: example-tls-secret`** → 这个 `example-tls-secret` 必须是一个包含证书的 Kubernetes Secret
- **后端 Pod 只需要处理 HTTP（不需要 TLS）**



**示例：TLS 透传（TLS Passthrough）**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
    - protocol: HTTPS
      port: 443
      name: passthrough-https
      tls:
        mode: Passthrough  # 直接将加密流量传递给后端
```

**解释**

- **`tls.mode: Passthrough`** → 说明 **Gateway 不处理 TLS，加密流量直接传给后端**
- **后端 Service 需要监听 443 端口，并自己处理 TLS**



**示例：mTLS（双向认证）**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
    - protocol: HTTPS
      port: 443
      name: mutual-tls
      tls:
        mode: Mutual  # 启用双向 TLS
        certificateRefs:
          - name: example-tls-secret  # 服务器证书
        options:
          clientCA: "ca-secret"  # 客户端 CA 证书，用于验证客户端证书
```

**解释**

- **`tls.mode: Mutual`** → Gateway 需要验证客户端证书
- **`certificateRefs.name: example-tls-secret`** → 服务器端 TLS 证书
- **`options.clientCA: ca-secret`** → 客户端 CA 证书（用于验证客户端）



###### 补充：addresses字段详解

**完整示例**

```bash
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: default
spec:
  gatewayClassName: nginx
  listeners:
    - protocol: HTTPS
      port: 443
      name: https
      tls:
        mode: Terminate               # 在 Gateway 终结 TLS
        certificateRefs:
          - name: example-tls-secret  # 这里是 Kubernetes Secret 名称
  addresses:                          # 客户端访问 192.168.1.100 时，流量会进入 Gateway
    - type: IPAddress                 # 指定 Gateway 绑定一个静态 IP（192.168.1.100）
      value: 192.168.1.100            # 具体的 IP 地址
```

在 Gateway API 的 `Gateway` 资源中，`addresses` 用于指定 **Gateway 绑定的网络地址**，即监听流量的 IP 地址或其他网络端点。

**`addresses.type` 可选值**

Gateway API 支持多种 `type`，具体如下：

| **值**         | **作用**                                                     |
| -------------- | ------------------------------------------------------------ |
| `IPAddress`    | 指定 Gateway 绑定的 **静态 IP**（适用于 MetalLB 或云提供商的静态 IP） |
| `NamedAddress` | 绑定一个 **云服务提供商的 IP 名称**（如 AWS Elastic IP，GCP Cloud Load Balancer） |
| `Hostname`     | 绑定到 **主机名**（如 `example.com`，用于 DNS 解析）         |
| `Service`      | 绑定到 **某个 Kubernetes Service**（一般用于 LoadBalancer 类型的 Service） |

**示例 1：使用 `IPAddress` 绑定静态 IP**

适用于 **裸机环境**（MetalLB 或手动分配 IP）。

```yaml
addresses:
  - type: IPAddress
    value: 192.168.1.100
```

**流量会通过 192.168.1.100 进入 Gateway**。



**示例 2：使用 `NamedAddress` 绑定云负载均衡 IP**

适用于 **云环境（AWS/GCP/AlibabaCloud）**。

```yaml
addresses:
  - type: NamedAddress
    value: my-cloud-lb-ip  # 绑定云提供商的负载均衡 IP 名称
```

这里的 **`my-cloud-lb-ip`** 由云提供商（如 AWS Elastic IP）管理。



**示例 3：使用 `Hostname` 绑定 DNS 名称**

适用于 **托管环境**（Cloudflare、Cloud Load Balancer）

```yaml
addresses:
  - type: Hostname
    value: gateway.example.com
```

这个 **`gateway.example.com`** 必须在 DNS 解析到 Gateway 的 IP。



**示例 4：使用 `Service` 绑定 Kubernetes Service**

适用于 **Kubernetes Service 负载均衡**。

```yaml
addresses:
  - type: Service
    value: my-gateway-service  # Gateway 绑定到 Service
```

**流量会通过 `my-gateway-service` 进入 Gateway**。



**什么时候用什么类型？**

| **场景**                   | **推荐 `type`** | **说明**                |
| -------------------------- | --------------- | ----------------------- |
| **裸机集群（MetalLB）**    | `IPAddress`     | 绑定本地 IP             |
| **云环境（AWS/GCP）**      | `NamedAddress`  | 绑定云提供商的 IP 名称  |
| **DNS 入口（Cloudflare）** | `Hostname`      | 绑定域名                |
| **内部 Service 负载均衡**  | `Service`       | 绑定 Kubernetes Service |



##### Path redirects

路径重定向使用 HTTP 路径修饰符来替换整个路径或路径前缀。例如，下面的 HTTPRoute 将向所有以 /cayenne 开头的 `redirect.example` 请求发出 302 重定向到 `/paprika`：

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-filter-redirect
spec:
  hostnames:
    - redirect.example
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /cayenne
      filters:
        - type: RequestRedirect
          requestRedirect:
            path:
              type: ReplaceFullPath             # ReplaceFullPath 会完全替换路径，而不是保留后缀路径
              replaceFullPath: /paprika
            statusCode: 302
```

```ABAP
如果客户端请求 redirect.example/cayenne，它会 302 重定向 到 redirect.example/paprika，这个是 正确的 ✅。
```

**举例验证**

| **原请求**                               | **是否匹配 `/cayenne` 规则？** | **最终重定向 URL**         |
| ---------------------------------------- | ------------------------------ | -------------------------- |
| `redirect.example/cayenne`               | ✅ **匹配**                     | `redirect.example/paprika` |
| `redirect.example/cayenne/`              | ✅ **匹配**                     | `redirect.example/paprika` |
| `redirect.example/cayenne/a/a.txt`       | ✅ **匹配**                     | `redirect.example/paprika` |
| `redirect.example/cayenne/a.txt`         | ✅ **匹配**                     | `redirect.example/paprika` |
| `redirect.example/cayenne/anything/else` | ✅ **匹配**                     | `redirect.example/paprika` |

**无论 `/cayenne` 后面是什么，都会被重定向到 `/paprika`，不会保留后缀路径** 🚨。



###### `requestRedirect.path.type` 的可选值及其含义

在 `HTTPRoute` 资源中，`requestRedirect.path.type` 用于指定 **如何修改路径**，它有以下 **三种可选值**：

| **可选值**           | **含义**                                                     | **示例**                                                     |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `ReplaceFullPath`    | **完整替换路径**，无论原始路径如何，都会被替换成固定值       | `/old/path` → `/new/path`                                    |
| `ReplacePrefixMatch` | **替换前缀**，仅替换匹配的路径前缀，保留后缀部分             | `/old/path/foo` → `/new/path/foo`                            |
| `ReplacePathMatch`   | **仅替换匹配部分的路径**，如果匹配的路径完全相同，则替换，否则不变 | `/old/path` → `/new/path` （但 `/old/path/foo` **不会改变**） |



**`ReplaceFullPath` —— 完全替换路径**

- **作用**：所有匹配到的请求路径都会被完全替换成新的路径，不管原路径后面有没有子路径
- **适用场景**：
  - 你希望所有匹配到的路径都跳转到一个 **固定的 URL**。
  - 例如：`/cayenne` 及其所有子路径都重定向到 `/paprika`。

**示例**

```yaml
filters:
  - type: RequestRedirect
    requestRedirect:
      path:
        type: ReplaceFullPath
        replaceFullPath: /paprika
      statusCode: 302
```

**结果**

| **原请求 URL**     | **最终重定向 URL** |
| ------------------ | ------------------ |
| `/cayenne`         | `/paprika`         |
| `/cayenne/foo`     | `/paprika`         |
| `/cayenne/bar/baz` | `/paprika`         |
| `/cayenne/a.txt`   | `/paprika`         |

📌 **无论 `/cayenne` 后面是什么，都会变成 `/paprika`**，后缀不会保留 🚨。



**`ReplacePrefixMatch` —— 仅替换路径前缀**

- **作用**：**只替换匹配的路径前缀，保留后缀部分**。
- **适用场景**：
  - 你希望 `/old/path/foo` 变成 `/new/path/foo`，而不是 `/new/path`。
  - 例如：把 `/cayenne/xxx` 变成 `/paprika/xxx`，但 `/cayenne` 仍然变成 `/paprika`。

**示例**

```yaml
filters:
  - type: RequestRedirect
    requestRedirect:
      path:
        type: ReplacePrefixMatch
        replacePrefixMatch: /paprika
      statusCode: 302
```

 **结果**

| **原请求 URL**     | **最终重定向 URL** |
| ------------------ | ------------------ |
| `/cayenne`         | `/paprika`         |
| `/cayenne/foo`     | `/paprika/foo`     |
| `/cayenne/bar/baz` | `/paprika/bar/baz` |
| `/cayenne/a.txt`   | `/paprika/a.txt`   |

📌 **路径后缀得到了保留！** ✅



**`ReplacePathMatch` —— 仅替换完全匹配的路径**

**作用**：如果路径 **完全匹配** 设定的值，就替换，否则不做改变。

**适用场景**：

- 你只想替换特定的路径，而不影响子路径。
- 例如：`/cayenne` 变成 `/paprika`，但 `/cayenne/foo` **不会改变**。

```yaml
filters:
  - type: RequestRedirect
    requestRedirect:
      path:
        type: ReplacePathMatch
        replacePathMatch: /paprika
      statusCode: 302
```

**结果**

| **原请求 URL**     | **最终重定向 URL** |
| ------------------ | ------------------ |
| `/cayenne`         | `/paprika`         |
| `/cayenne/foo`     | `/cayenne/foo`     |
| `/cayenne/bar/baz` | `/cayenne/bar/baz` |
| `/cayenne/a.txt`   | `/cayenne/a.txt`   |

📌 **只有 `/cayenne` 被重定向，子路径完全不变！** 🚀



##### HTTP Rewrite

重写会在将客户端请求代理到上游之前修改其组件。URLRewrite 过滤器可以更改上游请求的**主机名**和/**路径**。例如，以下 HTTPRoute 将接受 `https://rewrite.example/cardamom` 的请求，并将其上游发送到 `example-svc`，请求标头中的 `host: else.example` 而不是 `host: rewrite.example`。

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-filter-rewrite
spec:
  hostnames:
    - rewrite.example
  rules:
    - filters:
        - type: URLRewrite
          urlRewrite:
            hostname: elsewhere.example
      backendRefs:
        - name: example-svc
          weight: 1                            # 权重
          port: 80
```

路径重写也使用 HTTP 路径修饰符。下面的 HTTPRoute 将接受` https://rewrite.example/cardamom/smidgen` 的请求，并将对 `https://elsewhere.example/fennel` 的请求代理到 example-svc 上游。

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-filter-rewrite
spec:
  hostnames:
    - rewrite.example
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /cardamom
      filters:
        - type: URLRewrite
          urlRewrite:
            hostname: elsewhere.example
            path:
              type: ReplaceFullPath
              replaceFullPath: /fennel
      backendRefs:
        - name: example-svc
          weight: 1
          port: 80
```



#### HTTP traffic splitting 分流

HTTPRoute 资源允许您指定权重以在不同的后端之间转移流量。这对于在推出、金丝雀变更或紧急情况下分割流量非常有用。

`HTTPRoutespec.rules.backendRefs` 接受路由规则将向其发送流量的后端列表。这些后端的相对权重定义了它们之间的流量分割。以下 YAML 代码片段显示了如何将两个服务列为单个路由规则的后端。此路由规则将流量的 90% 分割到 foo-v1，10% 分割到 foo-v2。

![image-20250320161221624](../markdown_img/image-20250320161221624.png)

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: simple-split
spec:
  rules:
  - backendRefs:
    - name: foo-v1
      port: 8080
      weight: 90
    - name: foo-v2
      port: 8080
      weight: 10
```



##### 限制 Gateway 能够处理的 HTTPRoute 规则来源

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: prod-web
spec:
  gatewayClassName: example
  listeners:
  - protocol: HTTP
    port: 80
    name: prod-web-gw
    allowedRoutes:            # 用于限制 Gateway 能够处理的 HTTPRoute 规则来源
      namespaces:
        from: Same
```



##### 基于 http 头部字段进行分流

![image-20250320162612677](../markdown_img/image-20250320162612677.png)

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: foo-route
  labels:
    gateway: prod-web-gw
spec:
  hostnames:
  - foo.example.com
  rules:
  - backendRefs:
    - name: foo-v1
      port: 8080
  - matches:
    - headers:
      - name: traffic
        value: test
    backendRefs:
    - name: foo-v2
      port: 8080
```





#### Cross-Namespace routing 不同名称空间之间的路由 

**Gateway -> Route**：对名称空间没有限制（除非 **`allowedRoutes` 限制**）。

**Route -> Backend:** 对名称空间有限制，默认需要再同一个名称空间

![image-20250320170107687](../markdown_img/image-20250320170107687.png)



##### 补充：`allowedRoutes.namespaces.from` 字段的可选值

`allowedRoutes.namespaces.from` 字段用于控制 **哪些 Namespace 的 `HTTPRoute` 可以绑定到 `Gateway`**。

它有以下可选值：

1. **`Same`**（仅允许相同 Namespace）
2. **`Selector`**（允许特定 Label 选择的 Namespace）
3. **`All`**（允许所有 Namespace）



###### `Same`（仅允许相同 Namespace）

**含义：**

- 只允许和 `Gateway` **相同 Namespace** 的 `HTTPRoute` 绑定。
- **其他 Namespace 不能** 绑定这个 `Gateway`。

**🔹 适用场景：**

- **单租户环境**，只允许当前 Namespace 的服务使用该 `Gateway`。

**🔹 配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: web-gateway
  namespace: web
spec:
  gatewayClassName: example
  listeners:
    - protocol: HTTP
      port: 80
      name: web-gateway-listener
  allowedRoutes:
    namespaces:
      from: Same  # ✅ 只允许 web Namespace 下的 HTTPRoute 绑定
```

➡️ `web` Namespace 下的 `HTTPRoute` 可以绑定，但 `default`、`app` Namespace 不能使用。



###### `Selector`（允许特定 Namespace）

**含义：**

- 允许 **特定 Label 选择的 Namespace** 绑定 `Gateway`。
- 适用于**部分共享 Gateway** 的场景。

**🔹 适用场景：**

- **多租户环境**，不同团队的 `Namespace` 需要共享同一个 `Gateway`。

**🔹 配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: shared-gateway
  namespace: infra
spec:
  gatewayClassName: example
  listeners:
    - protocol: HTTP
      port: 80
      name: shared-listener
  allowedRoutes:
    namespaces:
      from: Selector  # ✅ 允许特定 Label 的 Namespace 绑定
      selector:
        matchLabels:
          team: frontend  # ✅ 只有带 team=frontend Label 的 Namespace 才能绑定
```

`web` 和 `app` Namespace 需要添加 Label 才能使用

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: web
  labels:
    team: frontend  # ✅ 允许绑定 Gateway
---
apiVersion: v1
kind: Namespace
metadata:
  name: app
  labels:
    team: frontend  # ✅ 允许绑定 Gateway
```

**➡️ 只有 `web` 和 `app` Namespace 能绑定这个 `Gateway`，其他不带 `team=frontend` 的不能用。**



###### `All`（允许所有 Namespace）

**含义：**

- **任何 Namespace** 的 `HTTPRoute` 都可以绑定这个 `Gateway`。
- **默认值**，如果 `allowedRoutes` 字段省略，则默认 `All`。

**🔹 适用场景：**

- **全局共享 Gateway**，允许整个集群的 `HTTPRoute` 使用。

**🔹 配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: global-gateway
  namespace: infra
spec:
  gatewayClassName: example
  listeners:
    - protocol: HTTP
      port: 80
      name: global-listener
  allowedRoutes:
    namespaces:
      from: All  # ✅ 允许所有 Namespace
```

**➡️ `default`、`web`、`app`、`test` 等 Namespace 的 `HTTPRoute` \**都可以\** 绑定这个 `Gateway`。**



**总结**

| `from` 选项  | 说明                                         | 适用场景         |
| ------------ | -------------------------------------------- | ---------------- |
| **Same**     | 仅允许**相同 Namespace** 的 `HTTPRoute` 绑定 | 单租户，严格隔离 |
| **Selector** | 允许带**特定 Label** 的 `Namespace` 绑定     | 多租户，部分共享 |
| **All**      | 允许所有 `Namespace` 绑定**（默认值）**      | 全局共享 Gateway |



##### 补充：HTTPRoute 资源中，HTTPRoute 和 Backend是否必须在同一名称空间

在 `HTTPRoute` 中，`backendRefs` 默认指向 **与 `HTTPRoute` 处于同一 `Namespace`** 的 `Service`。

###### 默认行为

如果 `backendRefs` 没有指定 `namespace`，它默认指向 **`HTTPRoute` 所在的 Namespace`** 的 `Service`

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-route
  namespace: app-ns   # ✅ HTTPRoute 在 app-ns Namespace 下
spec:
  parentRefs:
  - name: redirect-gateway
    sectionName: https
  hostnames:
  - redirect.example
  rules:
  - backendRefs:
    - name: example-svc  # ✅ 默认 app-ns/example-svc
      port: 80
```

➡ `example-svc` 默认会在 `app-ns` Namespace 里查找！



###### 如果 `backendRefs` 指定了 `namespace`

可以显式指定 `Service` 的 `namespace`，允许 `HTTPRoute` 访问其他 Namespace 下的 `Service`（**但 `Gateway` 需要允许跨 Namespace 绑定**）

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-route
  namespace: app-ns
spec:
  parentRefs:
  - name: redirect-gateway
    sectionName: https
  hostnames:
  - redirect.example
  rules:
  - backendRefs:
    - name: example-svc
      namespace: backend-ns  # ✅ 明确指定 backend-ns Namespace 的 Service
      port: 80
```

**➡ 这里 `HTTPRoute` 在 `app-ns`，但它的 `backendRefs` 绑定了 `backend-ns` 下的 `Service`！**



**关键点**

| **字段**                       | **默认行为**                                         | **可以改吗？**                                          |
| ------------------------------ | ---------------------------------------------------- | ------------------------------------------------------- |
| `backendRefs.name`             | 只查找 **`HTTPRoute` 同名 `Namespace`** 的 `Service` | ✅ 可以指定 `namespace`                                  |
| `backendRefs.namespace`        | **默认不跨 Namespace**                               | ✅ 可以手动指定                                          |
| `Gateway` 是否允许跨 Namespace | **默认只允许 Same `Namespace`**                      | ✅ 需要 `allowedRoutes.namespaces.from: All 或 Selector` |



##### Route Attachment

由于路由和 Gateway 在不同名称空间，所以在 parentRefs 中要指定 Gateway 的名称空间

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: store
  namespace: store-ns
spec:
  parentRefs:
  - name: shared-gateway
    namespace: infra-ns            # 因为Gateway和HTTPRoute不在同一名称空间，因此这里需要指定关联的Gateway的名称空间
  rules:
  - matches:
    - path:
        value: /store
    backendRefs:
    - name: store
      port: 8080
```



#### HTTP 请求头部字段修改

HTTP 标头修改是在传入请求中添加、删除或修改 HTTP 头部字段的过程。

要配置 HTTP 标头修改，请使用一个或多个 HTTP 过滤器定义 Gateway 对象。每个过滤器指定对传入请求进行的特定修改，例如添加自定义标头或修改现有标头。

要向 HTTP 请求添加标头，请使用 RequestHeaderModifier 类型的过滤器，并带有添加操作以及标头的名称和值：

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: header-http-echo
spec:
  parentRefs:
    - name: acme-gw
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /add-a-request-header
      filters:
        - type: RequestHeaderModifier
          requestHeaderModifier:
            add:
              - name: my-header-name
                value: my-header-value
      backendRefs:
        - name: echo
          port: 8080
```

要编辑现有标题，请使用设置操作并指定要修改的标题的值和要设置的新标题值。

```yaml
filters:
    - type: RequestHeaderModifier
      requestHeaderModifier:
        set:
          - name: my-header-name
            value: my-new-header-value
```

Headers can also be removed, by using the `remove` keyword and a list of header names.

```yaml
 filters:
    - type: RequestHeaderModifier
      requestHeaderModifier:
        remove: ["x-request-id"]
```



#### HTTP 响应头部字段修改

就像编辑请求标头很有用一样，响应标头也很有用。例如，它允许团队仅为某个后端添加/删除 cookie，这有助于识别之前重定向到该后端的某些用户。

另一个潜在的用例是，当你的前端需要知道它正在与后端服务器的稳定版本还是测试版本对话时，以便呈现不同的 UI 或相应地调整其响应解析

修改 HTTP 标头响应利用与修改原始请求非常相似的语法，尽管使用了不同的过滤器（ResponseHeaderModifier）。

可以添加、编辑和删除标题。可以添加多个标题，如下例所示：

```yaml
  filters:
    - type: ResponseHeaderModifier
      responseHeaderModifier:
        add:
        - name: X-Header-Add-1
          value: header-add-1
        - name: X-Header-Add-2
          value: header-add-2
        - name: X-Header-Add-3
          value: header-add-3
```





### TCP routing

Gateway API 旨在与多种协议配合使用，而 TCPRoute 就是这样一种路由，它允许管理 TCP 流量。

在此示例中，我们有一个 Gateway 资源和两个 TCPRoute 资源，它们按照以下规则分配流量：

- Gateway 端口 8080 上的所有 TCP 流都转发到 my-foo-service Kubernetes 服务的端口 6000。
- Gateway 端口 8090 上的所有 TCP 流都转发到 my-bar-service Kubernetes 服务的端口 6000。

在此示例中，将向 Gateway 应用两个 TCP 侦听器，以便将它们路由到两个单独的后端 TCPRoute，请注意，Gateway 上侦听器的协议设置为 TCP：

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-tcp-gateway
spec:
  gatewayClassName: my-tcp-gateway-class
  listeners:
  - name: foo
    protocol: TCP
    port: 8080
    allowedRoutes:
      kinds:
      - kind: TCPRoute
  - name: bar
    protocol: TCP
    port: 8090
    allowedRoutes:
      kinds:
      - kind: TCPRoute
---
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TCPRoute
metadata:
  name: tcp-app-1
spec:
  parentRefs:
  - name: my-tcp-gateway
    sectionName: foo
  rules:
  - backendRefs:
    - name: my-foo-service
      port: 6000
---
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TCPRoute
metadata:
  name: tcp-app-2
spec:
  parentRefs:
  - name: my-tcp-gateway
    sectionName: bar
  rules:
  - backendRefs:
    - name: my-bar-service
      port: 6000
```



#### `allowedRoutes.kinds.kind` 可选值及使用场景

在 `Gateway` 资源中，`allowedRoutes.kinds.kind` 用于 **定义 `Gateway` 能接受的路由类型**，确保 `Gateway` 只能绑定特定类型的 `Route`（如 `HTTPRoute`、`TCPRoute`、`TLSRoute` 等）。

```ABAP
默认 allowedRoutes.kinds 允许所有类型，但为了安全性，建议 显式指定 允许的 Route 类型。
```

**✅ 可选值**

| **值 (`kind`)** | **作用**                        | **适用场景**                                 |
| --------------- | ------------------------------- | -------------------------------------------- |
| `HTTPRoute`     | 允许 `Gateway` 绑定 `HTTPRoute` | Web 应用、API 服务                           |
| `TCPRoute`      | 允许 `Gateway` 绑定 `TCPRoute`  | 纯 TCP 流量，如数据库连接、MQTT              |
| `TLSRoute`      | 允许 `Gateway` 绑定 `TLSRoute`  | 需要 L4 TLS 透传的场景，如 `TLS Passthrough` |
| `GRPCRoute`     | 允许 `Gateway` 绑定 `GRPCRoute` | gRPC 服务，如微服务 RPC                      |
| `UDPRoute`      | 允许 `Gateway` 绑定 `UDPRoute`  | VoIP、DNS 解析等 UDP 服务                    |



**配置示例**

🟢 允许 `Gateway` 只绑定 `HTTPRoute`

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: web-gateway
spec:
  gatewayClassName: nginx
  listeners:
  - protocol: HTTP
    port: 80
    allowedRoutes:
      kinds:
      - kind: HTTPRoute  # ✅ 只允许绑定 HTTPRoute
```

**适用场景**

- 只允许 HTTP 路由流量
- 用于 Web 应用/API 服务器



🟢 允许 `Gateway` 绑定 `TCPRoute` 和 `TLSRoute`

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: tcp-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - protocol: TLS
    port: 443
    allowedRoutes:
      kinds:
      - kind: TCPRoute  # ✅ 允许 TCP 代理
      - kind: TLSRoute  # ✅ 允许 TLS 代理
```

**适用场景**

- 需要代理 TCP 连接，如数据库（MySQL、PostgreSQL）
- 需要 TLS Passthrough，如邮件服务器、VPN



🟢 允许 `Gateway` 绑定所有类型的 `Route`

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: multi-protocol-gateway
spec:
  gatewayClassName: istio
  listeners:
  - protocol: HTTP
    port: 80
    allowedRoutes:
      kinds:
      - kind: HTTPRoute
      - kind: TCPRoute
      - kind: TLSRoute
      - kind: GRPCRoute
      - kind: UDPRoute
```

**适用场景**

- 一个 `Gateway` 处理多种协议，如 Web API、数据库、VoIP
- 适用于多协议代理（如 Istio）



### TLSRoute

#### TLSRoute 在 Downstream 端解密 和 Upstream 端加密详解

###### Downstream 端解密 (TLS Termination)

**场景**

- **客户端 (browser/curl)** 使用 `HTTPS` 访问 `Gateway`。
- `Gateway` **解密** TLS 流量，并将 **纯 HTTP** 发送给后端 `Service` 进行处理。
- 适用于 Web 服务器、API 代理等场景。

**配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: tls-gateway
spec:
  gatewayClassName: istio
  listeners:
    - protocol: HTTPS
      port: 443
      tls:
        mode: Terminate  # ✅ 终结 TLS
        certificateRefs:
          - name: my-tls-secret  # Kubernetes Secret，包含 TLS 证书
```

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: TLSRoute
metadata:
  name: tls-route
spec:
  parentRefs:
    - name: tls-gateway
  rules:
    - backendRefs:
        - name: my-http-service
          port: 80  # ❗️发送纯 HTTP
```

**流量路径**

1️⃣ **客户端** 发起 `HTTPS` 请求 → `curl https://example.com`
2️⃣ **`Gateway` 终结 TLS**，使用 `my-tls-secret` 解密流量
3️⃣ **明文 HTTP** 转发到 `my-http-service:80` 处理请求



###### Upstream 端加密 (TLS Passthrough / TLS Origination)

`TLSRoute` 也可以用于 **透传 TLS** 或 **为上游重新加密 TLS**。

**场景 1: TLS 透传 (TLS Passthrough)**

- **客户端** 直接连接后端 `Service`，`Gateway` **不解密 TLS**，直接转发。
- 适用于 **邮件服务器 (IMAP, SMTP)**、**数据库 (MySQL, PostgreSQL)** 等应用。

**配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: passthrough-gateway
spec:
  gatewayClassName: istio
  listeners:
    - protocol: TLS
      port: 443
      tls:
        mode: Passthrough  # ✅ 透传 TLS
```

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: TLSRoute
metadata:
  name: tls-passthrough-route
spec:
  parentRefs:
    - name: passthrough-gateway
  rules:
    - backendRefs:
        - name: my-tls-service
          port: 443  # ❗️后端 `Service` 直接接收 TLS
```

**流量路径**

1️⃣ **客户端** `curl https://example.com`
2️⃣ **`Gateway` 不解密 TLS**，直接透传流量
3️⃣ **后端 `my-tls-service` 处理 TLS**，使用自己配置的证书解密



**场景 2: TLS 重新加密 (Upstream TLS Origination)**

- `Gateway` **解密 TLS**，但在转发给 `Service` 时 **重新加密 TLS**。
- 适用于 **安全要求较高的微服务环境**，避免在集群内传输明文流量。

**配置示例**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: tls-reencrypt-gateway
spec:
  gatewayClassName: istio
  listeners:
    - protocol: HTTPS
      port: 443
      tls:
        mode: Terminate  # ✅ 终结 TLS
        certificateRefs:
          - name: my-tls-secret
```

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: TLSRoute
metadata:
  name: tls-frontend-route
spec:
  parentRefs:
    - name: tls-reencrypt-gateway
  rules:
    - backendRefs:
        - name: my-secure-service
          port: 443
          tls:
            mode: Simple  # ✅ 重新加密
            certificateRefs:
              - name: backend-tls-secret
```

**流量路径**

1️⃣ **客户端** `curl https://example.com`
2️⃣ **`Gateway` 终结 TLS**，使用 `my-tls-secret` 解密
3️⃣ **`Gateway` 重新加密 TLS**，使用 `backend-tls-secret` 发送给 `my-secure-service`



**`mode` 选项总结**

| **TLS Mode**            | **描述**                             | **适用场景**       |
| ----------------------- | ------------------------------------ | ------------------ |
| `Terminate`             | `Gateway` 终结 TLS，转发明文 HTTP    | 普通 HTTPS 站点    |
| `Passthrough`           | 直接透传 TLS，`Service` 自己解密     | 邮件服务器、数据库 |
| `Simple` (Upstream TLS) | `Gateway` 先解密，然后重新加密后转发 | 内部微服务安全加密 |

```ABAP
Gateway支持双向认证
```



#### Wildcard（通配符证书） TLS Listeners

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: wildcard-tls-gateway
spec:
  gatewayClassName: example
  listeners:
  - name: foo-https
    protocol: HTTPS
    port: 443
    hostname: foo.example.com
    tls:
      certificateRefs:
      - kind: Secret
        group: ""
        name: foo-example-com-cert
  - name: wildcard-https
    protocol: HTTPS
    port: 443
    hostname: "*.example.com"
    tls:
      certificateRefs:
      - kind: Secret
        group: ""
        name: wildcard-example-com-cert
```

**Wildcard 证书的限制**

1. ❌ 不能跨级别子域

   ```ini
   CN = *.example.com
   ```

   **✅ 支持**：`api.example.com`, `blog.example.com`
   **❌ 不支持**：`sub.api.example.com`

   - **如果需要跨层级通配符证书**，可以使用 `*.api.example.com`。

2. **❌ 不能用于 `example.com` (裸域)**
   - 解决方案：**申请额外的 `example.com` 证书** 或 **使用 SAN 证书**。





#### 跨命名空间引用证书

在此示例中，网关配置为引用不同命名空间中的证书。这是通过在目标命名空间中创建的 **ReferenceGrant** 允许的。如果没有该 ReferenceGrant，跨命名空间引用将无效。

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: cross-namespace-tls-gateway
  namespace: gateway-api-example-ns1
spec:
  gatewayClassName: example
  listeners:
  - name: https
    protocol: HTTPS
    port: 443
    hostname: "*.example.com"
    tls:
      certificateRefs:
      - kind: Secret
        group: ""       # 这里可以省略，因为默认就是 core group
        name: wildcard-example-com-cert
        namespace: gateway-api-example-ns2
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant             # ReferenceGrant 和 Secret 创建在同一名称空间
metadata:
  name: allow-ns1-gateways-to-ref-secrets
  namespace: gateway-api-example-ns2
spec:
  from:
  # 上面的ReferenceGrant，不是针对某一个Gateway授权，而是针对Gateway所在的名称空间授权
  - group: gateway.networking.k8s.io    # 非核心 API 组（比如 Gateway、HTTPRoute、ReferenceGrant 等），必须显式声                                           明 group，否则解析失败。
    kind: Gateway
    namespace: gateway-api-example-ns1
  to:
  - group: ""     # 这里可以省略，因为默认就是 core group
    kind: Secret
```



##### 补充：`group` 字段的含义

在 Kubernetes **Gateway API** 以及 **ReferenceGrant** 资源中，`group` 字段用于指定 Kubernetes API 资源的 **API 组** (API Group)，也就是该资源所属的 API 组。

Kubernetes 资源的 **完整 API 组** 结构通常是：

```php
<kind>.<group>/<version>
```

**例如**：

- `Gateway` 属于 `gateway.networking.k8s.io/v1`
- `Secret` 属于 `core` API 组（`""` 代表 `core` 组）
- `ReferenceGrant` 属于 `gateway.networking.k8s.io/v1beta1`



**上述配置中的 `group` 的解释**

```yaml
tls:
  certificateRefs:
  - kind: Secret
    group: ""
    name: wildcard-example-com-cert
    namespace: gateway-api-example-ns2
```

- **group: `""`**
  - 这里 `""` 为空，表示 **Secret 资源** 来自 Kubernetes **Core API 组** (`v1`)。
  - `Secret` 属于 Kubernetes **核心 API**，因此 **API 组为空** (`""`)。
  - 完整路径：`Secret.v1` (即 `core/v1`)

```yaml
spec:
  from:
  - group: gateway.networking.k8s.io
    kind: Gateway
    namespace: gateway-api-example-ns1
```

- **group: `gateway.networking.k8s.io`**
  - 表示 **Gateway 资源**，它属于 `gateway.networking.k8s.io/v1` API 组。
  - 允许 `gateway-api-example-ns1` 中的 **Gateway 访问** `gateway-api-example-ns2` 里的 Secret。

```yaml
  to:
  - group: ""
    kind: Secret
```

- group: `""`
  - 表示目标资源是 **Secret**，属于 Kubernetes **核心 API 组** (`core/v1`)。



**如何确定 `group` 值**

可以使用 `kubectl api-resources` 命令，查看 API 组信息：

```bash
kubectl api-resources
```



#### TargetRefs and TLS

`BackendTLSPolicy` 是 **Kubernetes Gateway API** 中的一种扩展资源，用于“**验证后端 TLS 服务是否可信**”的！

```ABAP
再强调一遍: BackendTLSPolicy 并不是用于“建立 TLS 通信”的，而是用于“验证后端 TLS 服务是否可信”的！
也就是说：TLSRoute.backendRefs.tls 管“我怎么连过去”，BackendTLSPolicy 管“我信不信你”。
```

##### 示例 YAML 拆解说明

```yaml
apiVersion: gateway.networking.k8s.io/v1alpha3
kind: BackendTLSPolicy
metadata:
  name: tls-upstream-dev
spec:
  targetRefs:
    - kind: Service
      name: dev
      group: ""
  validation:
    wellKnownCACertificates: "System"
    hostname: dev.example.com
```

**作用概述：**

配置 Gateway 访问 `Service/dev` 时，使用 **HTTPS** 协议，**并信任系统根 CA**，**对服务端证书的域名进行校验**。



##### 字段详细说明

1. **`targetRefs`**

指定此策略要应用在哪个**后端服务（Service）**上。

```yaml
targetRefs:
  - kind: Service         # 应用于哪个类型的资源，必须是 Service
    name: dev             # Service 的名称
    group: ""             # group 为空表示 core 组（标准 Kubernetes 资源）
```

🔎 **用途**：指明是哪个 Service 使用 Upstream TLS。



2. **`validation`**

配置 TLS 的**验证规则**：

```yaml
validation:
  wellKnownCACertificates: "System"
  hostname: dev.example.com
```

**a) `wellKnownCACertificates: "System"`**

- 表示信任系统默认的根证书（如 Ubuntu/RHEL 中 `/etc/ssl/certs` 中的根证书）。

- 用于验证后端服务的 TLS 证书是合法颁发的。

- 支持的值（当前阶段）：

  | 值             | 含义                                                         |
  | -------------- | ------------------------------------------------------------ |
  | `"System"`     | 使用 **Gateway 所在节点操作系统** 的默认 CA 信任列表（通常是 `/etc/ssl/certs/ca-certificates.crt` 或等效路径） |
  | `null`（不填） | 不启用默认信任 CA。你需要通过 `caCertRefs` 字段自己指定可信 CA 证书 Secret。 |

       作用：用于**验证后端服务证书是否被可信 CA 签发**，防止中间人攻击，确保你信任的服务才被通信。

- 使用你自签的 CA 来校验后端证书：

  ```yaml
  validation:
    caCertRefs:
      - name: my-root-ca
        kind: Secret
        group: ""
    hostname: dev.internal.svc
  ```

**b) `hostname: dev.example.com`**

- 表示连接时需要校验后端服务器 TLS 证书中的 **CN/SAN 域名** 是否匹配 `dev.example.com`。

- 它会被验证匹配 **证书的 SAN（Subject Alternative Name）字段**，如果 SAN 没有设置，才会 fallback 到证书的 **Subject 的 Common Name (CN)** 字段。

  | 优先级                              | 匹配字段 |
  | ----------------------------------- | -------- |
  | 1️⃣ SAN (Subject Alternative Name)    |          |
  | 2️⃣ CN (Common Name) – 已过时，但兼容 |          |

- 你后端证书长这样（用 `openssl x509 -text` 查看）：

  ```ruby
  Subject: CN = dev.example.com
  X509v3 Subject Alternative Name:
      DNS:dev.example.com, DNS:*.example.com
  ```

  那么配置：

  ```yaml
  validation:
    hostname: dev.example.com
  ```

  是 ✅ 匹配成功的。

- 类似于 curl 中的 `--resolve` 或浏览器的证书校验行为。

📌 如果证书的 SAN 字段中没有这个域名，会导致连接失败。





### 实战案例

#### 把 HTTP 请求重定向为 HTTPS

1️⃣ **用RequestRedirect 这个Filter实现重定向，Gateway 要有 HTTP 和 HTTPS 两个前端Listener**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: redirect-gateway
spec:
  gatewayClassName: foo-lb
  listeners:
  - name: http
    protocol: HTTP
    port: 80
  - name: https
    protocol: HTTPS
    port: 443
    tls:
      mode: Terminate
      certificateRefs:
      - name: redirect-example
```

**2️⃣该 Route 把 HTTP 重定向为 HTTPS**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-filter-redirect
spec:
  parentRefs:
  - name: redirect-gateway       # Gateway.name
    sectionName: http            # 匹配 Gateway 资源的 Listeners.name
  hostnames:
  - redirect.example
  rules:
  - filters:
    - type: RequestRedirect
      requestRedirect
        scheme: https
        statusCode: 301
```

**3️⃣下一个 Route 把 HTTPS 请求路由到相应的业务 Service**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: https-route
  labels:
    gateway: redirect-gateway
spec:
  parentRefs:
  - name: redirect-gateway
    sectionName: https
  hostname:
  - redirect.example
  rules:
  - backendRefs:
    - name: example-svc
      port: 80                # 这里backend没有指定名称空间，默认和gateway在同一个名称空间
```





#### Gateway 双向 TLS 认证 (Mutual TLS, mTLS) 

**场景**

- **客户端 (Browser, API Consumer)** 需要 **提供客户端证书** 以证明身份。
- **`Gateway` 验证客户端证书**，并决定是否允许访问。
- **`Gateway` 终结 TLS** 并将请求转发给后端 `Service`。



**具体实现**

##### 1️⃣ 创建 CA 证书 & 服务器、客户端证书

```bash
# 生成 CA 证书
openssl req -new -x509 -days 365 -keyout ca.key -out ca.crt -subj "/CN=MyCA"

# 生成服务器证书 (用于 Gateway)
openssl req -newkey rsa:2048 -nodes -keyout server.key -out server.csr -subj "/CN=gateway.example.com"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365

# 生成客户端证书 (用于 API 调用)
openssl req -newkey rsa:2048 -nodes -keyout client.key -out client.csr -subj "/CN=ClientApp"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

##### **2️⃣ 创建 Kubernetes Secret**

```bash
# 存储 Gateway 服务器端证书
kubectl create secret tls gateway-server-tls --cert=server.crt --key=server.key -n default

# 存储 CA 证书 (用于验证客户端)
kubectl create secret generic gateway-ca-secret --from-file=ca.crt=ca.crt -n default
```

##### 3️⃣ 配置 `Gateway`

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: mtls-gateway
  namespace: default
spec:
  gatewayClassName: istio
  listeners:
    - name: https-mtls
      protocol: HTTPS
      port: 443
      tls:
        mode: Terminate  # ✅ 终结 TLS
        certificateRefs:
          - name: gateway-server-tls  # 服务器证书
        options:
          clientCertificate: Required  # ✅ 强制客户端提供证书
          clientCertificateRefs:
            - name: gateway-ca-secret  # ✅ 客户端证书 CA
```

**解释**

- `mode: Terminate` → `Gateway` 终结 TLS，解密 HTTPS 流量。
- `clientCertificate: Required` → `Gateway` 强制要求客户端提供证书。
- `clientCertificateRefs: gateway-ca-secret` → 通过 **CA 证书** 验证客户端身份。



##### 4️⃣ 配置 `TLSRoute`

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: TLSRoute
metadata:
  name: secure-api
  namespace: default
spec:
  parentRefs:
    - name: mtls-gateway
  rules:
    - backendRefs:
        - name: my-secure-service
          port: 443  # 发送到后端 HTTPS
          tls:
            mode: Simple  # ✅ 重新加密 TLS
            certificateRefs:
              - name: backend-tls-secret  
              
---
apiVersion: gateway.networking.k8s.io/v1alpha3
kind: BackendTLSPolicy
spec:
  targetRefs:
    - kind: Service
      name: my-secure-service
  validation:
    wellKnownCACertificates: "System"
    hostname: my-service.example.com
```

**解释**

- **`Gateway` 终结 TLS**，但后端 `Service` **仍然使用 HTTPS**。
- **`mode: Simple`** → `Gateway` 重新加密 TLS，并发送给后端。
- **目前支持的 `mode` 值（来自官方文档）：**

  | 值            | 含义                                                         |
  | ------------- | ------------------------------------------------------------ |
  | `Terminate`   | Gateway 终止 TLS，向后端发送明文 HTTP（常用于 HTTPS Termination） |
  | `Passthrough` | Gateway 不处理 TLS，**原样转发 TLS 流量**给后端              |
  | `Simple`      | Gateway 会 **主动重新加密**，即与客户端和后端都用各自的 TLS 通信 |

- 引用的 `backend-tls-secret` 是一个 **TLS 类型的 Kubernetes Secret**，里面一般包含这几个字段：

  | 字段             | 内容                             | 说明                                                        |
  | ---------------- | -------------------------------- | ----------------------------------------------------------- |
  | `tls.crt`        | 客户端证书（Client Certificate） | Gateway 用来向后端 Pod 证明自己身份                         |
  | `tls.key`        | 客户端证书对应的私钥             | Gateway 在与后端进行 TLS 握手时使用的私钥                   |
  | `ca.crt`（可选） | 后端的根证书或中间证书           | 用于验证后端 Pod 的服务端证书是否合法（属于单向认证一部分） |



##### 5️⃣ 客户端访问测试

```bash
curl -v --key client.key --cert client.crt https://gateway.example.com
```

✅ 如果客户端证书有效，则 `Gateway` 允许请求
❌ 如果客户端未提供证书，则 `403 Forbidden`



**总结**

| **功能**                      | **作用**               |
| ----------------------------- | ---------------------- |
| `mode: Terminate`             | `Gateway` 终结 TLS     |
| `clientCertificate: Required` | 强制客户端提供证书     |
| `clientCertificateRefs`       | 指定客户端证书 CA      |
| `mode: Simple`                | `Gateway` 重新加密 TLS |

🚀 **这样就完成了 Kubernetes Gateway API 的双向 TLS 认证！** 🚀