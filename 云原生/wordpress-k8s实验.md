## 使用k8s实现wordpress架构
### 创建wordpress的service网络
```shell
kubectl create svc loadbalancer wordpress --tcp 80:80 --dry-run=client -o yaml > wordpress-mysql-svc-deployment.yaml
```

### 创建deployment类型编排的wordpress
```shell
kubectl create deployment wordpress --image registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache--dry-run=client -o yaml >> wordpress-mysql-svc-deployment.yaml kubectl cre
```

### 创建mysql的service网络
```shell
kubectl create svc clusterip mysql --tcp 3306:3306 --dry-run=client -o yaml > wordpress-mysql-svc-deployment.yaml
```

### 创建mysql的deployment类型
```shell
kubectl create deployment mysql --image registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle --dry-run=client -o yaml >> wordpress-mysql-svc-deployment.yaml 
```

### 在最开始定义一个名称空间，整理yaml文件如下
```yaml
apiversion: v1
kind: namespace
metadata:
  name: wordpress
---
apiversion: v1
kind: service
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
  selector:
    app: wordpress
  type: loadbalancer

---
apiversion: apps/v1
kind: deployment
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  progressdeadlineseconds: 600
  replicas: 1
  revisionhistorylimit: 10
  selector:
    matchlabels:
      app: wordpress
    type: rollingupdate
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache--dry-run=client
        imagepullpolicy: ifnotpresent
        name: wordpress

---

apiversion: v1
kind: service
metadata:
  creationtimestamp: null
  labels:
    app: mysql
  name: mysql
spec:
  ports:
  - name: 3306-3306
    port: 3306
    protocol: tcp
    targetport: 3306
  selector:
    app: mysql
  type: clusterip

---
apiversion: apps/v1
kind: deployment
metadata:
  labels:
    app: mysql
  name: mysql
spec:
  replicas: 1
  selector:
    matchlabels:
      app: mysql
  template:
    metadata:
      creationtimestamp: null
      labels:
        app: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
```

### 在执行资源清单的时候，指定一开始创建的namespace，并记得把环境变量写上
```yaml
apiversion: v1
kind: namespace
metadata:
  name: wordpress
---
apiversion: v1
kind: service
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  ports:
  - name: 80-80
    port: 80
    protocol: tcp
    targetport: 80
  selector:
    app: wordpress
  type: loadbalancer

---
apiversion: apps/v1
kind: deployment
metadata:
  labels:
    app: wordpress
  name: wordpress
spec:
  replicas: 1
  selector:
    matchlabels:
      app: wordpress
  template:
    metadata:
      labels:
        app: wordpress
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/wordpress:php8.2-apache
        imagepullpolicy: ifnotpresent
        name: wordpress
        env:
        - name: wordpress_db_host
          value: mysql.wordpress.svc.cluster.local.
        - name: wordpress_db_user
          value: wordpress
        - name: wordpress_db_password
          value: "123456"
        - name: wordpress_db_name
          value: wordpress

---
apiversion: v1
kind: service
metadata:
  labels:
    app: mysql
  name: mysql
spec:
  ports:
  - name: 3306-3306
    port: 3306
    protocol: tcp
    targetport: 3306
  selector:
    app: mysql
  type: clusterip
---
apiversion: apps/v1
kind: deployment
metadata:
  name: mysql
spec:
  replicas: 1
  selector:
    matchlabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: registry.cn-beijing.aliyuncs.com/wangxiaochun/mysql:8.0.29-oracle
        name: mysql
        env: 
        - name: mysql_root_password
          value: "123456"
        - name: mysql_database
          value: "wordpress"
        - name: mysql_user
          value: wordpress
        - name: mysql_password
          value: "123456"
```
### 启用资源清单
```shell
kubectl apply -f wordpress-mysql-svc-deployment.yaml -n wordpress 
```