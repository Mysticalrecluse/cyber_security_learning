## 项目目录
- 网站根目录是指存放网站的第一层文件夹，内部包含当前网站的所有素材，包含HTML、CSS、图片、Javascript等等。

- 根目录
  - images文件夹：存放固定使用的图片素材，例如；logo、样式修饰图等待
  - uploads文件夹：存放非固定使用的图片素材，例如；商品图、宣传图等需要上传的图片
  - CSS文件夹：存放CSS文件(link标签引入)
    - base.css：基础公共样式，例如：清除默认样式，设置网页基本样式
    - index.css：首页CSS样式
  - index.html：首页HTML文件

## 网页制作思路
- 布局思路
  - 先整体在局部
  - 从外到内
  - 从上到下
  - 从左到右

- CSS实现思路
  - 画盒子，调整盒子范围 -> 宽高背景色
  - 调整盒子位置 -> flex布局、内外边距
  - 控制图片、文字内容样式

## header区域-布局
### logo制作技巧
- 功能：
  - 点击跳转到首页
  - 搜索引擎优化：提升网页百度搜索排名

- 实现方法：
  - 标签结构：h1 > a > 网站名称（搜索关键字）
  - CSS样式
  ```css
  .logo a {
    display:block;
    width: 195px;
    height: 41px;
    background-image: url(../images/logo.png);
    /* 隐藏文字 */
    font-size: 0;
  }
  ```

### 导航制作技巧（nav）
- 导航功能：
  - 单击跳转页面

- 实现方法：
  - 标签结构：ul > li * 3 > a
  - 优势：避免推砌a标签，网站搜索排名降级
  - 布局思路
    - li设置 右侧 margin
    - a 设置 左右 padding

### 搜索区域（search）
- 实现方法
  - 标签结构：search > input + [a | button]

### banner区域-布局
- 结构
  - 通栏banner > 版心 > .left + .right

#### 左侧侧导航
- 实现方法：
  - 结构标签：.left > ul > li*9 > a

- 布局思路
  - a 默认状态；背景图为白色箭头