# 数据结构
- 概述
  - 数据结构 = 数据定义 + 结构操作 （学习重点）
  - 数据结构就是定义一种性质，并且维护这种性质（使用数据结构的重点）

## 顺序表和链表
### 顺序表：结构定义
![Alt text](alg_images/image2.png)

- 包含3部分
  - 一段连续的存储区，表示顺序表存储元素的地方
  - 一个整型的变量，用来标记顺序表的大小 (size)
  - 一个整型的变量，用来标记顺序表中存储元素的数量 (count)

### 顺序表的插入操作
![Alt text](alg_images/image3.png)

### 顺序表的删除操作
![Alt text](alg_images/image4.png)

### 顺序表代码
```C
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

/* 顺序表的结构定义*/
typedef struct vector { // 元数据
    int size, count;
    int *data; // 顺序表首地址
} vector; 
// 结构体中包含了3个数据分别是：顺序表的大小，数据的数量以及存储数据的首地址

/* 初始化顺序表 */
vector *getNewVector(int n) {
    vector *p = (vector *)malloc(sizeof(vector)); // 元数据地址
    p->size = n;
    p->count = 0;
    p->data = (int *)malloc(sizeof(int) * n); // 数据首地址
    return p;
}

/* 使用之后，销毁该顺序表 */
void clear(vector *v) {
    if (v == NULL) return ;
    free(v->data); //销毁数据内存
    free(v); // 销毁元数据内存
    return ;
}

/* 顺序表的扩容操作 */
int expand(vector *v) {
    if (v == NULL) return 0;
    printf("expand v from %d to %d\n", v->size, v->size * 2); // 2倍扩容法
    int *p = (int *)realloc(v->data, sizeof(int) * 2 * v->size);
    if (p == NULL) return 0;
    v->data = p;
    v->size *= 2;
    return 1;
}
/*
*   realloc()的功能：重新进行内存分配
*   realloc()的工作过程：
*   1. 先在原内存地址上，试着向后进行延展（策略1：首地址不变，大小变大）
*   2. 如果无法向后扩展，则realloc会找一片新内存，将原内存的数据拷贝过来，并返回新内存地址（策略2）
*   3. 策略1和2都不成功，realloc返回null,且原内存不动，但是此时，源地址信息丢失，因为返回的是null
*
* */

/* 顺序表的插入操作 */
int insert(vector *v, int pos, int val) {
    if (pos < 0 || pos > v->count) return 0; // 判断插入位置的合法性
    if (v->size == v->count && !expand(v)) return 0; // 判断顺序表是否有空间插入数据
    // 注意逆序遍历
    for (int i = v->count, i >= pos, i--) {
        v->data[i + 1] = v->data[i];
    }
    v->count += 1;
    v->data[pos] = val;
    return 1;
}

/* 顺序表的删除操作 */
int erase(vector *v, int pos) {
    if (pos < 0 || pos > v->count) return 0; // 判断删除位置的合法性
    for (int i = pos + 1, i < v->count, i++) {
        v->data[i - 1] = v->data[i];
    }
    v->count -= 1;
    return 1;
}

/* 输出顺序表的数据 */
void output_vector(vector *v) {
    int len = 0;
    for (int i = 0; i < v->size; i++) {
        len += printf("%3d", i);
    }
    printf("\n");
    for (int i = 0; i < len; i++) {
        printf("-");
    }
    printf("\n");
    for (int i = 0; i < v->count; i++) {
        printf("%3d", v->data[i]);
    }
    printf("\n\n");
    return ;
}

int main() {
    srand(time(0));
    #define MAX_OP 20
    vector *v = getNewVector(2);
    for (int i = 0; i < MAX_OP; i++) {
        int op = rand() % 4, pos, val, ret;
        switch (op) {
            case 0: 
            case 1:
            case 2: {
                pos = rand() % (v->count + 2);
                val = rand() % 100;
                ret = insert(v, pos, val);
                printf("insert %d at %d to vetor = %d\n", 
                    val, pos, ret);
            };break;
            case 3:{
                pos = rand() % (v->count + 2);
                ret = erase(v, pos);
                printf("erase item at %d in vector = %d\n", 
                    pos, ret);
            };break;
        }
        output_vector(v);
    }
    clear(v);
    return 0;
}
```

### 链表：结构定义
- 结构定义：
  - 链表是由若干个节点（逻辑结构上）串联在一起的
  - 逻辑结构串联的实现：
    - 每个节点存储两个信息，一个是数据，一个是下一个节点的地址（指针）

### 两种链表
- 无头链表
  - 头部不存储信息，仅存储第一个节点的地址

- 有头链表
  - 头部有存储数据的区域，但是不使用，仅使用部分空间存储节点地址

### 虚拟头节点
- 定义：
  - 一般有头链表的头节点，称为虚拟头节点（重要编程技巧）

### 链表的操作
- 链表的插入操作：
  - 假设一个链表中有4个节点，将node节点插入到第2个节点的位置
    - 第一步：创建一个指针p，指向待插入位置的前一个节点
    - 第二步：node节点上的地址信息，指向原2号节点
    - 第三步：指针p指向的节点的地址信息，指向node节点
    - 完成链表的插入操作
  - 易错点：
    - 如果先将指针p指向的节点地址指向node节点
    - 此时整个链表失去了指向原2号节点的地址信息，因为原二号节点的地址信息记录在1号节点（也就是p指向的节点上，现在它改变了），从而造成了内存泄漏

### 链表代码演示
```C
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define DL 3
#define STR(n) #n
#define DIGIT_LEN_STR(n) "%" STR(n) "d"

// 链表结构定义
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// 结构操作
// 初始化链表
Node *getNewNode(int val) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = val;
    p->next = NULL;
    return p;
}

// 链表插入
// 无头链表在插入过程中，首地址可能发生改变，因此返回值是新链表的首地址
Node *insert(Node *head, int pos, int val) {
    // 如果插入位置是头地址的话，整个链表的首地址发生改变
    if (pos == 0) {
        Node *p = getNewNode(val);
        p->next = head;
        return p;
    }
    // 如果插入的不是头地址，则需要先找到待插入位置的前一个元素
    Node *p = head;
    for (int i = 1; i < pos; i++) p = p->next;
    Node *node = getNewNode(val);
    node->next = p->next;
    p->next = node;
    return head;
}


// 销毁链表
void clear(Node *head) {
    if (head == NULL) return ;
    for (Node *p = head, *q; p; p = q) {
        q = p->next;
        free(p);
    }
    return ;
}

// 输出链表操作
void output_linklist(Node *head, int flag) {
    int n = 0;
    for (Node *p = head; p; p = p->next) n += 1;
    for (int i = 0; i < n; i++) {
        printf(DIGIT_LEN_STR(DL), i);
        printf("  "); // 留出小箭头的位置
    }
    printf("\n");
    for (Node *p = head; p; p = p->next) {
        printf(DIGIT_LEN_STR(DL), p->data);
        printf("->");
    }
    printf("\n");
    if (flag == 0) printf("\n\n");
    return ;
}

// 链表的查找
int find(Node *head, int val) {
    Node *p = head;
    int n = 0;
    while (p) {
        if (p->data == val) {
            output_linklist(head, 1);
            int len = n * (DL + 2) + 2;
            for (int i = 0; i < len; i++) printf(" ");
            printf("^\n");
            for (int i = 0; i < len; i++) printf(" ");
            printf("|\n");
            return 1;
        };
        n += 1;
        p = p->next;
    }
    return 0;
}

int main() {
    srand(time(0));
    #define MAX_OP 20
    Node *head = NULL;
    for (int i = 0; i < MAX_OP; i++) {
        int pos = rand() % (i + 1), val = rand() % 100, ret;
        printf("insert %d at %d to linklist\n", val, pos);
        head = insert(head, pos, val);
        output_linklist(head, 0);
    }
    int val;
    while(~scanf("%d", &val)) { // ~是按位取反的意思
        if (!find(head,val)) {
            printf("not found\n");
        }
    }
    clear(head);
    /*
        关于while(~scanf("%d", &val)) 的详细解析
        当 scanf 成功读取一个整数并将其存储在 val 中时，它返回 1。按位取反 ~1 产生的结果不是 0（因为所有位都被取反了），所以循环继续。
        当 scanf 到达文件末尾（例如，用户输入了 EOF 字符，通常是 Ctrl+D 或 Ctrl+Z），它返回 EOF（即 -1）。由于在大多数系统中 -1 的二进制表示是全 1，因此按位取反后变成全 0，即 0。这使得 while 循环的条件变为 false，循环终止。
        因此，while(~scanf("%d", &val)) 实际上是一种检测输入结束的方式。只要用户不输入 EOF 字符，循环就会继续。这是一种在 C 语言中常见的用于从标准输入读取值的模式。

        因此：while(~scanf("%d", &val))等价于while(scanf("%d", &val) != EOF)
    */

    return 0;
}
```

### 有头链表精简插入模块
```C
Node *insert(Node *head, int pos, int val) {
    // 定义一个虚拟头节点
    // 有头链表的优势：同时整合了插入的两种情况
    Node new_head, *p = &new_head, *node = getNewNode(val);
    new_head.next = head;
    for (int i = 0; i < pos; i++) p = p->next; // 有无虚拟头的关键所在
    // 如果没有虚拟头的话，当插入到0位置时，就找不到0位置的前一个节点
    // 因为0位置没有节点，仅是一个记录首地址的指针
    node->next = p->next;
    p->next = node;   
    return new_head.next;
}
```

### 循环链表和双向链表
- 单向循环链表：
  - 最后一个节点指向第一个节点
  - 注意：
    - 头指针指向最后一个节点（将最后一个节点，看作是有头链表的虚拟节点）

- 双向链表：
  - 链表的结构定义中，多加一个p->pre,指向前一个节点
  ![Alt text](images/image05.png)
  - 第一个节点的pre和最后一个节点的next都指向null

### 反转链表
- 解题思路1：
  - 用指针遍历链表中的每一个节点，然后将其插入到新链表的头部，实现链表反转
  ```C
  ListNode *reverseList(ListNode *head) {
        ListNode new_head, *p = head, *q;
        new_head.next = NULL;
        while (p) {
            q = p->next;
            p->next = new_head.next;
            new_head.next = p;
            p = q;
        }
        return new_head.next;
  }
  ``` 

- 解题思路2：
  - 将第一个节点后面的链表全部反转，然后将第一个节点移动到最后
  - 依次递归实现
  - 递归函数的语义就是反转链表，返回反转后链表的首地址 
  ```C
  ListNode *reverseList(ListNode *head) {
        if (head == NULL && head->next == NULL) return head;
        ListNode *tail = head->next;
        ListNode *new_head = reverseList(head->next);
        head->next = NULL;
        tail->next = head;
        return new_head;
  }
  ```

### 判断循环链表
- 解题思路：创建两个速率不同的指针，根据两个指针在同一起点开始走，后面是否能相遇来判断链表是否是循环链表
```C
Bool hasCycle(struct ListNode *head) {
    struct ListNode *p = head, *q = head;
    while (q == NULL && q->next == NULL) {
        p = p->next;
        q = q->next->next;
        if (p == q) return true;
    }
    return false;
}
```

### 判断快乐数
- 快乐数定义：
  - 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
  - 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
  - 如果这个过程 结果为 1，那么这个数就是快乐数。   

- 示例：
```
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

82->68->100->1
```
- 解题思路：
  - 将快乐数的推断过程看作是一个链表结果，将最终结果1看作是NULL，如果该链表有环，则证明不是快乐数，否则证明是快乐数

- 代码实现
```C
int getNext(int x) {
    int d, y = 0;
    while (x) {
        d = x % 10;
        y += d * d;
        x = x / 10;
    }
    return y;
} 

bool isHappy(int n) {
    int p = n, q = n;
    while (q != 1) {
        p = getNext(p);
        q = getNext(getNext(q));
        if (q == p && q != 1) return false;
    } 
    return true;
}
```

### 旋转链表
- Leecode-61
- 答案：
```C
int getLen(struct ListNode* head) {
    int n = 0;
    while (head) {
        n++;
        head = head->next;
    }
    return n;
}

struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL) return head;
    int n = getLen(head);
    k %= n;
    if (k == 0) return head;
    struct ListNode *p = head, *q = head;
    for (int i = 0; i <= k; i++) p = p->next;
    // q指向分割的节点， 即新链表头部的前一个节点
    while (p) p = p->next, q = q->next;
    p = q->next;
    q->next = NULL;
    q = p;
    while (q->next != NULL) q = q->next;
    q->next = head;
    return p;
}
```

- 解题思路2：
```C
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head == NULL) return head;
    // 计算链表节点数量
    int n = 0;
    struct ListNode *p = head, *q = head, *s = head, *e = head;
    while (p) {
        p = p->next;
        n++;
    }
    k %= n;
    if (k == 0) return head;
    // 末尾节点
    int tail = n - k;

    // 起始节点
    int start = n - k + 1;

    for (int i = 1; i < tail; i++) q = q->next; // q指向tail
    s = q->next;
    q->next = NULL;
    e = s;
    while (e->next != NULL) e = e->next;
    e->next = head;

    return s;


}
```

### 删除链表倒数第n个节点
- 解题思路1（简单）
```C
// Lecode-19
int nodeCount(struct ListNode* head) {
    int n = 0;
    while (head) {
        head = head->next;
        n++;
    }
    return n;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // 鉴于提示，此处不考虑空链表和n合法性的问题
    int count = nodeCount(head);
    n = count - n + 1;
    struct ListNode new_head, *p = &new_head, *q;
    new_head.next = head;
    for (int i = 1; i < n; i++) p = p->next;
    q = p->next;
    p->next = q->next;
    free(q);
    return new_head.next;

}
```
- 解题思路2：双指针等距移动法
```C
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // 鉴于提示，此处不考虑空链表和n合法性的问题
    struct ListNode new_head, *p = &new_head, *q = p;
    new_head.next = head;
    for (int i = 0; i <= n; i++) p = p->next;
    while (p) p = p->next, q = q->next;
    p = q->next;
    q->next = q->next->next;
    free(p);
    return new_head.next;
}
```

### 环形链表2
- 题目
  - 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
- 解题思路
```C
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *slow = head, *fast = head;

    // 使用快慢指针找到环中的一个点
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            // 找到环中的一个点
            struct ListNode *slow2 = head;
            // 从头节点和环中的相遇点同时出发，相遇点即为环的开始
            while (slow2 != slow) {
                slow = slow->next;
                slow2 = slow2->next;
            }
            return slow2; // 或 return slow;
        }
    }
    // 没有环
    return NULL;
}
```

### 反转链表2
- 题目：
  - 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

- 解题思路1(独立完成)
```C
struct ListNode* reverseList(struct ListNode *head) {
    if (head == NULL || head->next == NULL) return head;
    struct ListNode *tail = head->next;
    struct ListNode* new_head = reverseList(head->next);
    head->next = NULL;
    tail->next = head;
    return new_head;
}

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    struct ListNode new_head, *p = &new_head, *q = p;
    struct ListNode *l, *r;
    new_head.next = head;
    // 得到left的前一个节点地址
    for (int i = 1; i < left; i++) p = p->next;
    // 记录left节点地址
    l = p->next;
    // 得到right的节点地址
    for (int i = 0; i < right; i++) q = q->next;
    r = q->next;
    // 记录好数据后，将中间链切断并表反转
    struct ListNode *head2;
    head2 = l;
    q->next = NULL;
    reverseList(head2);
    p->next = q;
    l->next = r;
    return new_head.next;
}
```

- 解题思路2：
```C
struct ListNode* reverseList(struct ListNode *head) {
    if (head == NULL || head->next == NULL) return head;
    struct ListNode *new_head = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;
    return new_head;
}

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (left == right) return head;

    struct ListNode new_head, *prev = &new_head;
    new_head.next = head;
    struct ListNode *tail = NULL;

    // 移动到left的前一个节点
    for (int i = 0; i < left - 1; i++) {
        prev = prev->next;
    }

    // 记录left和right节点
    struct ListNode *left_node = prev->next;
    struct ListNode *right_node = left_node;

    for (int i = left; i < right; i++) {
        right_node = right_node->next;
    }

    tail = right_node->next;

    // 切断链表，进行反转
    right_node->next = NULL;
    prev->next = reverseList(left_node);

    // 连接反转后的链表
    left_node->next = tail;

    return new_head.next;
}

```
- 解题思路3（重点：递归）
```C
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (left == 1 && right == 1) return head;
    if (left != 1) {
        head->next = reverseBetween(head->next, left - 1, right - 1);
    } else {
        struct ListNode* tail = head->next;
        struct ListNode* new_head = reverseBetween(head->next, left, right - 1);
        head->next = tail->next;
        tail->next = head;
        head = new_head;
    }
    return head;

}
// 将大问题，分解成具有相同结构的小问题，然后递归处理
```

## 队列和栈
### 队列-结构讲解
![Alt text](images/image06.png)

- 只允许队首出元素，队尾入元素（顺序表允许在任意位置添加删除元素）

- 队列的三个定义
  - size：整个队列的长度
  - head：指向队首的指针 (闭)
  - tail：指向队尾的后一位的指针（开），空位置，不包含元素

- 队列特点：
  - 先进先出（first in first out）

- 队列的结构操作
  - 出队操作（pop）：头指针head向后移动一位 
  ![Alt text](images/image07.png)
  - 入队操作（push）：将入队元素插入队尾，然后尾指针tail向后移动一位
  ![Alt text](images/image08.png)

- 队列的假溢出
![Alt text](images/image09.png)

- 队列假溢出解决方案：循环队列
![Alt text](images/image10.png)

### 队列-代码演示
- 重点：高级数据结构中，对于基础数据结构，数据结构之间的封装

### 顺序表实现-队列
```C
#include<stdio.h>
#include<time.h>
#include<stdlib.h>

typedef struct Vector {
    int size;
    int count;
    int *data;
} Vector;

typedef struct Queue {
    Vector *data;
    int size, head, tail, count;
} Queue;

Vector *initVector(int n) {
    Vector *v = (Vector *)malloc(sizeof(Vector));
    v->size = n;
    v->count = 0;
    v->data = (int *)malloc(sizeof(int) * n);
    return v;
}

int insertVector(Vector *v, int pos, int val) { 
    if (pos < 0 || pos > v->count) return 0;
    v->data[pos] = val;
    v->count += 1;
    return 1;
}

Queue *initQueue(int n) {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->data = initVector(n);
    q->size = n;
    q->head = q->tail = q->count = 0;
    return q;
}

int push(Queue *q, int val) {
    if (q->count == q->size) return 0;
    insertVector(q->data, q->tail, val);
    q->tail += 1;
    if (q->tail == q->size) q->tail = 0; // 循环队列
    // 或者q->tail %= q->size;
    q->count += 1;
    return 1;
}

int vectorSeek(Vector *v, int n) {
    if (n < 0 || n > v->size) return -1;
    return v->data[n];
}

// 查看队首元素
int front(Queue *q) {
    return vectorSeek(q->data, q->head);
}

// 判空操作
int empty(Queue *q) {
    return q->count == 0;
}

int pop(Queue *q) {
    if (empty(q)) return 0;
    q->head += 1;
    q->count -= 1;
    return 1;
}

void clearVector(Vector *v) {
    if (v == NULL) return ;
    free(v->data);
    free(v);
    return ;
}

void clearQueue(Queue *q) {
    if (q == NULL) return ;
    clearVector(q->data);
    free(q);
    return ;
}

void outputQueue(Queue *q) {
    printf("Queue: ");
    for (int i = 0; i < q->count; i++) {
        printf("%4d", vectorSeek(q->data, (q->head + i) % q->size));
    }
    printf("\n\n");
    return ;
}

int main() {
    srand(time(0));
    #define MAX_OP 10
    Queue *q = initQueue(5);
    for (int i = 0; i < MAX_OP; i++) {
        int op = rand() % 5, val = rand() % 100;
        switch (op) {
            case 0:{
                printf("front of Queue is %d\n", front(q));
                pop(q);
                break;
            }
            case 1:
            case 2:
            case 3:
            case 4:{
                printf("push %d in %d\n", val, q->tail);
                push(q, val);
                break;
            }
        }
        outputQueue(q);
    }
    clearQueue(q);

    return 0;
}
```

### 链表实现-队列
```C
// 独立实现
#include<stdio.h>
#include<time.h>
#include<stdlib.h>

typedef struct Node {
    int val;
    struct Node *next;
} Node;

typedef struct Queue {
    int count;
    Node *head;
    Node *tail;
} Queue;


Queue *initQueue() {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    Node *vir_head = (Node *)malloc(sizeof(Node));
    vir_head->next = NULL;
    q->head = vir_head;
    q->tail = vir_head;
    q->count = 0;
    return q;
}

Node *getNode(int val) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->val = val;
    p->next = NULL;
    return p;
}

void push(Queue *q, int val) {
    if (q == NULL) return ;
    Node *p = getNode(val);
    if (q->count == 0) {
        q->head->next = p;
        q->tail = p;
    } else {
        q->tail->next = p;
        q->tail = p;
    }
    q->count += 1;
    return ;
}

void pop(Queue *q) {
    if (q->count == 0) return ;
    Node *p = q->head->next;
    q->head->next = q->head->next->next;
    free(p);
    q->count -= 1;
    return ;
}

void clearQueue(Queue *q) {
    Node *p = q->head->next;
    while (p) {
        Node *p1 = p;
        p = p->next;
        free(p1);
    }
    free(q);
    return ;
}

void outputQueue(Queue *q) {
    Node *p = q->head->next;
    while (p) {
        printf("%4d->", p->val);
        p = p->next;
    }
    printf("\n\n");
    return ;
}

int main() {
    srand(time(0));
    Queue *q = initQueue();
    #define MAX_OP 10
    for (int i = 0; i < MAX_OP; i++) {
        int op = rand() % 5, val = rand() % 100;
        switch (op) {
            case 0: {
                printf("pop a item %d\n", q->head->next->val);
                pop(q);
            } break;
            case 1:
            case 2:
            case 3:
            case 4: {
                printf("push a item %d\n", val);
                push(q, val);
            } break;
        }
        outputQueue(q);
    }
    clearQueue(q);
    return 0;
}
```

### 链表实现-队列2
```C
// 正确答案
#include<stdio.h>
#include<stdlib.h>
#include<time.h>


typedef struct Node {
    int val;
    struct Node *next;
} Node;

typedef struct LinkList {
    Node head, *tail;
} LinkList;

typedef struct Queue {
    LinkList *l;
    int count;
} Queue;

Node *getNode(int val) {
    Node *p = (Node *)malloc(sizeof(Node));
    p->val = val;
    p->next = NULL;
    return p;
}

LinkList *initLinkList() {
    LinkList *l = (LinkList *)malloc(sizeof(LinkList));
    l->head.next = NULL;
    l->tail = &(l->head);
    return l;
}

int frontLinkList(LinkList *l) {
    if (l->head.next == NULL) return 0;
    return l->head.next->val;
}

int insertTail(LinkList *l, int val) {
    Node *node  = getNode(val);
    l->tail->next = node;
    l->tail = node;
    return 1;
}

int earseHead(LinkList *l) {
    if (l->head.next == NULL) return -1;
    Node *p = l->head.next;
    l->head.next = l->head.next->next;
    if (l->tail == p) l->tail = &(l->head);
    free(p);
    return 1;
}

void clearLinkList(LinkList *l) {
    Node *p = l->head.next, *q;
    while (p) {
        q = p->next;
        free(p);
        p = q;
    }
    free(l);
    return ;
}

Queue *initQueue() {
    Queue *p = (Queue *)malloc(sizeof(Queue));
    p->l = initLinkList();
    p->count = 0;
    return p;
}

int empty(Queue *p) {
    return p->count == 0;
}

int front(Queue *p) {
    if (empty(p)) return -1;
    return frontLinkList(p->l);
}

int push(Queue *p, int val) {
    insertTail(p->l, val);
    p->count += 1;
    return 1;
}

int pop(Queue *p) {
    earseHead(p->l);
    p->count -= 1;
    return 1;
}



void clearQueue(Queue* q) {
    if (q == NULL) return ;
    clearLinkList(q->l);
    free(q);
    return ;
}

void outputQueue(Queue *q) {
    Node *p = q->l->head.next;
    while (p) {
        printf("%4d->", p->val);
        p = p->next;
    }
    printf("\n\n");
    return ;
}

int main() {
    srand(time(0));
    Queue *q = initQueue();
    #define MAX_OP 10
    for (int i = 0; i < MAX_OP; i++) {
        int op = rand() % 5, val = rand() % 100;
        switch (op) {
            case 0: {
                if (!empty(q)) {
                    printf("pop a item %d\n", q->l->head.next->val);
                    pop(q);
                }
            } break;
            case 1:
            case 2:
            case 3:
            case 4: {
                printf("push a item %d\n", val);
                push(q, val);
            } break;
        }
        outputQueue(q);
    }
    clearQueue(q);
    return 0;
}
``` 

### 栈-结构讲解
![Alt text](images/image11.png)

- 栈的结构特点：
  - 先进后出：first in last out (FILO)

### 栈-操作
- 出栈
![Alt text](images/image12.png)

- 入栈
![Alt text](images/image13.png)

### 栈-代码实现
```C
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

typedef struct Stack {
    int *data;
    int size, top;
} Stack;

Stack *initStack(int n) {
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->size = n;
    s->top = -1;
    s->data = (int *)malloc(sizeof(int) * n);
    return s;
}

int empty(Stack *s) {
    return s->top == -1;
}

int top(Stack *s) {
    if (empty(s)) return -1;
    return s->data[s->top];
}

int push(Stack *s, int val) {
    if (s->top + 1 == s->size) return -1;
    s->top += 1;
    s->data[s->top] = val;
    return 1;
}

int pop(Stack *s) {
    if (empty(s)) return -1;
    s->top -= 1;
    return 1;
}

void clearStack(Stack *s) {
    if (s == NULL) return ;
    free(s->data);
    free(s);
    return ;
}

void outputStack(Stack *s) {
    printf("Stack : ");
    for (int i = s->top; i >= 0; i--) {
        printf("%4d", s->data[i]);
    }
    printf("\n\n");
    return ;
}

int main() {
    srand(time(0));
    Stack *s = initStack(10);
    #define MAX_OP 10
    for (int i = 0; i < MAX_OP; i++) {
        int op = rand() % 4, val = rand() % 100;
        switch (op) {
            case 0: {
                printf("pop Stack: item = %d\n", top(s));
                pop(s);
            } break;
            case 1:
            case 2:
            case 3: {
                printf("push Stack: item = %d\n", val);
                push(s, val);
            } break;
        }
        outputStack(s);
    }
    clearStack(s);
    return 0;
}
```

### 用栈模拟括号匹配过程
- 遇到左括号就进栈

- 遇到右括号就和栈顶的左括号匹配，如果匹配成功，则栈顶元素出栈

- 如果匹配失败，则说明括号序列不合法

- 代码实现
```C
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

typedef struct Stack {
    char *data;
    int size, top;
} Stack;

Stack *initStack(int n) {
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->size = n;
    s->top = -1;
    s->data = (char *)malloc(sizeof(char) * n);
    return s;
}

int empty(Stack *s) {
    return s->top == -1;
}

char top(Stack *s) {
    if (empty(s)) return -1;
    return s->data[s->top];
}

int push(Stack *s, char val) {
    if (s->top + 1 == s->size) return -1;
    s->top += 1;
    s->data[s->top] = val;
    return 1;
}

int pop(Stack *s) {
    if (empty(s)) return -1;
    s->top -= 1;
    return 1;
}

void clearStack(Stack *s) {
    if (s == NULL) return ;
    free(s->data);
    free(s);
    return ;
}

void slove(char str[]) {
    int flag = 1;
    Stack *s = initStack(100);
    for (int i = 0; str[i]; i++) {
        if (str[i] == '(' || str[i] == '[' || str[i] == '{') {
            push(s, str[i]);
        } else {
            switch (str[i]) {
                case ')': {
                    if (top(s) == '(') pop(s);
                    else flag = 0;
                } break;
                case ']': {
                    if (top(s) == '[') pop(s);
                    else flag = 0;
                } break;
                case '}': {
                    if (top(s) == '{') pop(s);
                    else flag = 0;
                } break;
            }
        if (flag == 0) break;
        }
    }
    if (flag == 0 || !empty(s)) {
        printf("error\n");
    } else {
        printf("success\n");
    }                                   
    clearStack(s);
}

int main() {
    Stack *s = initStack(100);
    char str[100];
    while (~scanf("%s", str)) {
        slove(str);
    }
    return 0;
}
```

### 栈的深入理解
- 简化问题，如果只有一种括号()，然后判断括号是否合法，不使用栈结构

- 解题方法1：
```C
bool isValid(char *s) {
    int32_t lnum = 0, rnum = 0;
    int32_t len = strlen(s);
    for (int32_t i = 0; i < len; i++) {
        swtich (s[i]) {
            case '(': ++lnum; break;
            case ')': ++rnum; break;
            default : return false;
        }
        if (lnum >= rnum) continue;
        return false;
    }
    return lnum == rnum;
}
```

- 解题方法2：
```C
// 遇到左括号加1，遇到右括号减1，判断lnum是否小于0，以及最后是否等于0
bool isValid(char *s) {
    int32_t lnum = 0;
    int32_t len = strlen(s);
    for (int32_t i = 0; i < len; i++) {
        switch (s[i]) {
            case '(': ++lnum; break; // 类似于入栈
            case ')': --lnum; break; // 类似于出栈
            default : return false;
        }
        if (lnum >= 0) continue;
        return false;
    }
    return lnum == 0;
}
```

- 由上述代码深入思考
  - 加1代表进栈，抽象为发生了一件事情
  - 减1代表出栈，抽象为解决了一件事情
  - 一对括号()，抽象为一个完整的事件
  - （（）），抽象为一种事件的完全包含关系
  - 抽象理解((1)(2))
    - 要完成一个大事件，需要完成大事件包含的两个小事件
    - 先完成小事件1，再完成小事件2，继而完成整个大事件
    ```C
    // 根据上述表述，可以抽象为程序执行过程
    int main() {
        func1();
        func2();
        return 0;
    }
    // 总结：无论是程序还是现实问题，如果满足类似上述的主从包含关系的问题，大概率需要使用栈解决
    ```

### 栈理解练习-模拟程序调用
- 问题：
  - 给定一篇代码，并希望你能找到指定函数第一次被调用时的调用链，将其打印出来；当然，你有可能会发现给定的函数没有在代码中出现，那么你应该打印一行“NOT REFERENCED”并结束你的程序。
  - 样例输入
  ```
    5 // 表示下面5行是代码
    fun1()
    fun2()
    return
    fun3()
    fun4()
    fun4() // 求func4()的调用链
  ```
  - 样例输出
  ```
  fun1()->fun3()->fun4()
  ```

- 代码实现
```C
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct Stack {
    char **data;
    int size, top;
} Stack;

Stack *initStack(int n) {
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->data = (char **)malloc(sizeof(char*) * n);
    s->size = n;
    s->top = -1;
    return s;
}

int empty(Stack *s) {
    return s->top == -1;
}

int push(Stack *s, char *str) {
    if (s == NULL || str == NULL) return -1;
    if (s->top + 1 == s->size) return -1;
    s->top += 1;
    s->data[s->top] = str;
    return 1;
}

int pop(Stack *s) {
    if (empty(s)) return -1;
    s->top -= 1;
    return 1;
}

void clearStack(Stack *s) {
    if (s == NULL) return ;
    free(s->data);
    free(s);
    return ;
}

int main() {
    int n, flag = 0;
    scanf("%d", &n);
    Stack *s = initStack(n * 2);
    char *str[n];
    for (int i = 0; i < n; i++) {
        str[i] = (char *)malloc(sizeof(char) * 50);
        scanf("%50s", str[i]);
    }
    char target[50];
    scanf("%s", target);
    
    for (int i = 0; i < n; i++) {
        if (strcmp(str[i], target) == 0) {
            push(s, str[i]);
            flag = 1;
            break;
        } 
        if (strcmp(str[i], "return") == 0) {
            pop(s);
        } else {
            push(s, str[i]);
        }
    }

    if (flag) {
        for (int i = 0; i <= s->top; i++) {
            if (i > 0) printf("->");
            printf("%s", s->data[i]);
        }
    } else {
        printf("NOT REFERENCED\n");
    }

    printf("\n");

    // 释放内存
    for (int i = 0; i < n; i++) {
        free(str[i]);
    }

    clearStack(s);
    return 0;
}
```

### 2020年数据结构考研题41题
- 题目：
  - 定义三元组（a,b, c）（a,b,c 均为正数）的距离 D=|a-b|+|b-c|+|c-a|。给定 3 个非空整数集合 S1, S2 ,S3, 按升序分别存储在 3 个数组中。请设计一个尽可能高效的算法，计算并输出所有可能的三元组（a, b, c）（a∈S1,b∈S2,c∈S3）中的最小距离。例如 S1={-1, 0, 9}, S2={-25，-10，10，11}，S3={2，9，17，30，41}，则最小距离为 2，相应的三元组为（9，10，9）。

  - 程序中的主要部分已经帮你写好了，你只需要将如下代码拷贝到你的环境中，并且补充 func函数功能即可。函数功能描述如下：

- 代码实现
```C++
#include<iostream>
#include <cstdlib>
#include <queue>
using namespace std;

int min_num(int a, int b, int c) {
    if (a > b) swap(a, b);
    if (a > c) swap(a, c);
    return a;
}


int func(queue<int> que1, queue<int> que2, queue<int> que3) {
    int ans = 0x3f3f3f3f;
    while (!que1.empty() && !que2.empty() && !que3.empty()) {
        int a = que1.front(), b = que2.front(), c = que3.front();
        int temp_ans = abs(a - b) + abs(b - c) + abs(a - c);
        if (temp_ans < ans) ans = temp_ans;
        int d = min_num(a, b, c);
        if (a == d) que1.pop();
        if (b == d) que2.pop();
        if (c == d) que3.pop();
    }
    return ans;
}

int main() {
    int m, n, k, x;
    queue<int> que1, que2, que3;
    cin >> m >> n >> k;
    for (int i = 0; i < m; i++) {
        cin >> x;
        que1.push(x);
    }
    for (int i = 0; i < n; i++) {
        cin >> x;
        que2.push(x);
    }
    for (int i = 0; i < k; i++) {
        cin >> x;
        que3.push(x);
    }
    cout << func(que1, que2, que3) << endl;
    return 0;
}
```

### 火车入栈问题
- 问题：
  - ​有 n 列火车按 1 到 n 的顺序从东方左转进站，这个车站是南北方向的，它虽然无限长，只可惜是一个死胡同，而且站台只有一条股道，火车只能倒着从西方出去，而且每列火车必须进站，先进后出。
  - ​进站的火车编号顺序为 1∼n，现在请你按火车编号从小到大的顺序，输出前 20 种可能的出站方案。
- 代码实现
```C
#include<stdio.h>
#include "stack.h" // 自建数据结构头文件

int arr[25], vis[25] = {0};

int isValid(int *arr, int n) {
    Stack *s = initStack(25);
    int x = 1;
    for (int i = 0; i < n; i++) {
        if (emptyStack(s) || topStack(s) < arr[i]) {
            while (x <= arr[i]) pushStack(s, x), x++;
        }
        if (emptyStack(s) || topStack(s) != arr[i]) return 0;
        popStack(s);
    }
    return 1;
}

void print_one_res(int n) {
    for (int i = 0; i < n; i++) {
        if (i) printf(" ");
        printf("%d", arr[i]);
    }
    printf("\n");
    return ;
}

void f3(int i, int n) {
    if (i == n) {
        if (isValid(arr, n)) print_one_res(n);
        return ;
    }
    for (int k = 1; k <= n; k++) {
        if (vis[k]) continue;
        arr[i] = k;
        vis[k] = 1;
        f3(i + 1, n);
        vis[k] = 0;
    }
    return ;
}

int main() {
    int n;
    scanf("%d", &n);
    f3(0,n);
    return 0;
}
```

### 括号画家
- 解题方法1
```C
#include<stdio.h>
#include<string.h>
#include "stack.h"

int Maxarr(int *arr, int size) {
    int max = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] > max) max = arr[i];
    }
    return max;
}

int main() {
    int flag = 0, j = 0;
    char inp[10000];
    int arr[10000] = {0}; // 初始化为0
    Stack *s = initStack(10000);
    scanf("%s", inp);
    int len = strlen(inp);

    for (int i = 0; i < len; i++) {
        if (inp[i] == '(' || inp[i] == '[' || inp[i] == '{') {
            pushStack(s, inp[i]);
        } else {
            if (!emptyStack(s) && ((inp[i] == ')' && topStack(s) == '(') ||
                                   (inp[i] == ']' && topStack(s) == '[') ||
                                   (inp[i] == '}' && topStack(s) == '{'))) {
                popStack(s);
                flag += 2;
            } else {
                arr[j++] = flag;
                flag = 0;
                while (!emptyStack(s)) popStack(s); // 重置栈
            }
        }
    }
    arr[j] = flag; // 处理最后的合法序列

    int res = Maxarr(arr, j + 1);
    printf("%d\n", res);
    clearStack(s); // 清理栈
    return 0;
}

// 上述解题方法错误
// ((({}[]((() 在这种情况下，得到的结果是6，因为连续((()这种情况，上述程序并不能识别将flag即使清0
```

- 解题方法2
```C
#include <stdio.h>
#include <string.h>
#include "stack.h" // 假设这个头文件中定义了您的栈结构和相关函数
// 注意栈的数组类型为int，而不是char

int main() {
    char inp[10000];
    scanf("%s", inp);
    int n = strlen(inp), maxLen = 0;
    Stack *s = initStack(n + 1);
    pushStack(s, -1);  // 初始索引，用于长度计算(思维小难点)

    for (int i = 0; i < n; i++) {
        if (inp[i] == '(' || inp[i] == '[' || inp[i] == '{') {
            pushStack(s, i);  // 有效的开括号，推入其索引
        } else {
            // 确保栈非空并且顶部字符与当前字符匹配
            if (!emptyStack(s) && ((inp[i] == ')' && inp[topStack(s)] == '(') ||
                                   (inp[i] == ']' && inp[topStack(s)] == '[') ||
                                   (inp[i] == '}' && inp[topStack(s)] == '{'))) {
                popStack(s);  // 匹配的情况，弹出栈
                if (!emptyStack(s)) {
                    int currentLen = i - topStack(s);
                    maxLen = (currentLen > maxLen) ? currentLen : maxLen;
                }
            } else {
                while (!emptyStack(s)) popStack(s);  // 不匹配，清空栈
                pushStack(s, i);  // 将当前索引作为新的参考点(思维小难点)
            }
        }
    }

    printf("%d\n", maxLen);
    clearStack(s);
    return 0;
}
```

- 解题思路3：
```C
#include <stdio.h>
#include <string.h>
#include "stack.h" // 假设这个头文件中定义了您的栈结构和相关函数
// 注意栈的数组类型为int，而不是char

int main() {
    char str[100005];
    int match[100005] = {0};
    Stack *s = initStack(10000);
    scanf("%s", str + 1);
    for (int i = 1; str[i]; i++) {
        switch (str[i]) {
            case '(':
            case '[':
            case '{': pushStack(s, i); break; // 压入索引
            case ')': {
                if (!emptyStack(s) && str[topStack(s)] == '(') {
                    match[topStack(s)] = i;
                    popStack(s);
                } else {
                    pushStack(s, i); // 判断非法后，阻断栈
                }
            } break;
            case ']': {
                if (!emptyStack(s) && str[topStack(s)] == '[') {
                    match[topStack(s)] = i;
                    popStack(s);
                } else {
                    pushStack(s, i); // 判断非法后，阻断栈
                }
            } break;
            case '}': {
                if (!emptyStack(s) && str[topStack(s)] == '{') {
                    match[topStack(s)] = i;
                    popStack(s);
                } else {
                    pushStack(s, i); // 判断非法后，阻断栈
                }
            } break;
        }
    }

    // 第二部分
    int tmpans = 0, ans = 0, i = 1;
    while (str[i]) {
        if (match[i]) {
            tmpans += match[i] - i + 1;
            i = match[i] + 1;
        } else {
            i++;
            tmpans = 0;
        }
        ans = (tmpans > ans) ? tmpans : ans;
    }
    printf("%d\n", ans);
	 clearStack(s);
    return 0;

}
```
### 循环队列
- 使用顺序表实现
```C
typedef struct Vector {
    int *data;
    int size, count;
} Vector;


typedef struct {
    Vector *data;
    int size, count, head, tail;
} MyCircularQueue;

Vector *initVector(int size) {
    Vector *v = (Vector *)malloc(sizeof(Vector));
    if (v == NULL) return NULL; // 检查内存分配是否成功
    v->data = (int *)malloc(sizeof(int) * size); // 为 data 分配内存
    if (v->data == NULL) { // 检查内存分配是否成功
        free(v);
        return NULL;
    }
    v->size = size;
    v->count = 0;
    return v;
}


int insertVector(Vector *v, int pos, int val) {
    if (pos < 0 || pos > v->count) return 0;
    if (v->size == v->count) {
        // 扩展 Vector 的容量
        int newSize = v->size * 2;
        int *newData = (int *)realloc(v->data, newSize * sizeof(int));
        if (!newData) return 0;
        v->data = newData;
        v->size = newSize;
    }
    for (int i = v->count - 1; i >= pos; i--) {
        v->data[i + 1] = v->data[i];
    }
    v->data[pos] = val;
    v->count += 1;
    return 1;
}

int vectorSeek(Vector *v, int n) {
    if (n < 0 || n > v->size) return -1;
    return v->data[n];
}

void clearVector(Vector *v) {
    if (v == NULL) return ;
    free(v->data);
    free(v);
    return ;
}


MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *q = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    q->data = initVector(k);
    q->size = k;
    q->count = q->head = q->tail = 0;
    return q;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (obj->count == obj->size) return false;
    obj->data->data[obj->tail] = value;
    obj->tail = (obj->tail + 1) % obj->size; // 更新 tail
    obj->count += 1;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (obj->count == 0) return false;
    obj->head = (obj->head + 1) % obj->size;
    obj->count -= 1;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    if (obj->count == 0) return -1;
    return vectorSeek(obj->data, obj->head);;
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (obj->count == 0) return -1;
    int rearIndex = (obj->tail - 1 + obj->size) % obj->size; // 计算实际的 rear 索引
    return obj->data->data[rearIndex];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->count == 0;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->count == obj->size;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    if (obj == NULL) return ;
    clearVector(obj->data);
    free(obj);
    return ;
}
```

- 针对性型修改后
```C
typedef struct Vector {
    int *data;
    int size, count;
} Vector;


typedef struct {
    Vector *data;
    int size, count, head, tail;
} MyCircularQueue;

Vector *initVector(int size) {
    Vector *v = (Vector *)malloc(sizeof(Vector));
    if (v == NULL) return NULL; // 检查内存分配是否成功
    v->data = (int *)malloc(sizeof(int) * size); // 为 data 分配内存
    if (v->data == NULL) { // 检查内存分配是否成功
        free(v);
        return NULL;
    }
    v->size = size;
    v->count = 0;
    return v;
}


int insertVector(Vector *v, int val) {
    if (v->count == v->size) return 0; // 检查是否有空间插入新元素
    v->data[v->count] = val; // 在末尾添加元素
    v->count += 1;
    return 1;
}

int vectorSeek(Vector *v, int n) {
    if (n < 0 || n > v->size) return -1;
    return v->data[n];
}

void clearVector(Vector *v) {
    if (v == NULL) return ;
    free(v->data);
    free(v);
    return ;
}


MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *q = (MyCircularQueue*)malloc(sizeof(MyCircularQueue));
    q->data = initVector(k * 2); // 确保顺序表空间足够
    q->size = k;
    q->count = q->head = q->tail = 0;
    return q;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (obj->count == obj->size) return false;
    obj->data->data[obj->tail] = value;
    obj->tail = (obj->tail + 1) % obj->size; // 更新 tail
    obj->count += 1;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (obj->count == 0) return false;
    obj->head = (obj->head + 1) % obj->size;
    obj->count -= 1;
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    if (obj->count == 0) return -1;
    return vectorSeek(obj->data, obj->head);;
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (obj->count == 0) return -1;
    int rearIndex = (obj->tail - 1 + obj->size) % obj->size; // 计算实际的 rear 索引
    return obj->data->data[rearIndex];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->count == 0;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->count == obj->size;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    if (obj == NULL) return ;
    clearVector(obj->data);
    free(obj);
    return ;
}
```

## 树与二叉树
### 树形结构
![Alt text](images/image14.png)

- 推导
  - 绿色部分为单项链表
  - N叉树定义：每个节点最多指向N个子节点（例图中每个节点最多指向3个节点，即为三叉树）
  ```C
  // 三叉树最简单的定义形式
  typedef struct Node {
    int data;
    struct Node *next[3]; // N叉树改成*next[N]即可
  } Node, *tree;

  // 由此得出：单向链表结构是树形结构的特例
  ```
### 树的基本概念

![Alt text](images/image15.png)
- 树的深度和高度（概念相同）：
  - 都是从头节点算起，向下指向的最长链表结构的长度，即为树的深度（高度）

- 节点的深度和高度
  - 节点的深度：从头节点算起，到节点的距离，即为节点的深度
    - 例如，上图，4节点的深度为1
  - 节点的高度：从相关节点的叶子节点开始数，不包含当前节点
    - 例如，上图，4节点的高度为3

- 节点的度
  - 当前节点的子节点数量 （例如：上图节点1的度是3，节点4的度是2）
  - 细化概念
    - 入度：有几个节点指向我， 树形结构中，根节点入度为0，其他都为1
    - 出度：我指向几个节点，树形结构中的度指的就是出度

- 树形结构中，节点数量 = 边数 + 1 （未来很重要的一个可利用性质）

### 树形结构的深度理解
- 如何使用树形结构进行问题建模
  - 树形结构的节点代表【集合】
  - 树形结构的边代表【关系】

### 树形结构的两种遍历
- 广度优先遍历（层序遍历）
![Alt text](images/image16.png)
在队列中，将一个节点弹出的同时，将它的子节点全部压入队列，从而依次遍历所有节点
![Alt text](images/image17.png)

- 深度优先遍历
  - 使用栈结构进行遍历
  - 在一个栈中，将节点压入，如果该节点有未压入的子节点，就将该子节点压入栈中，然后看该子节点是否未压入栈中的子节点，如果有，一次压入栈中，直到子节点下没有子子节点，则将该节点弹出，
  然后向上回溯，重复上述过程
  ![Alt text](images/image18.png)
  - 将整个出栈入栈的过程整理到一个时间段中
  ![Alt text](images/image19.png)
  - 可以通过判断节点对应的时间序列的包含关系，来判断一个节点是否是另一个节点的子节点


# 算法
## 复杂度
### 时间复杂度
- 大O表示法
  - 用常数1取代运行时间中的所有加法常数
  - 在修改后的运行次数函数中，只保留最高阶项
  - 如果最高阶项存在且不是1，则去除与这个项目相乘的常数
  ```
  示例：
  3n + 100的时间复杂度
  step1：3n + 1, 用常数1取代加法常数100
  step2：3 * n ^ 1 + 1 * n ^ 0 -> 3n  只保留最高阶项
  step3: 3n -> n  如果最高阶项不是1，则去除与这个项目相乘的常数

  最终的到的时间复杂度就是O(n)

  ```

- O(1)时间复杂度示例；
```c++
int main() {
    int a1, n, d, sum = 0;
    cin >> a1 >> n >> d;
    sum = (a1 + a1 + (n - 1) * d) * n / 2;
    cout << sum << endl;
    return 0;
}
```

- O(n)时间复杂度示例
```C++
int main() {
    int a1, n, d, sum = 0;
    cin >> a1 >> n >> d;
    for (int i = a1, j = 0; j < n; i += d, j++) {
        sum += 1;
    }
    cout << sum << endl;
    return 0;
}
```

- O(n^2)时间复杂度示例
```C++
int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // TODO
        }
    }
    return 0;
}
```

- O(logn)时间复杂度示例
```C++
int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i *= 2) {
        cout << i << endl;
    }
    return 0;
}
```

- O(nm)时间复杂度
```C++
int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // TODO
        }
    }
    return 0;
}
```

- O(n + m)时间复杂度
```C++
int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cout << i << endl;
    }
    for (int i = 0; i < m; i++) {
        cout << i << endl;
    }
    return 0;
}
```
### 空间复杂度


## 递归函数
- 概述：
  - 自己调用自己的函数
  
### 阶乘
- 代码示例(阶乘)
```C
#include<stdio.h>

// 阶乘函数
int f(int n) {
  if (n == 1) return 1;
  return n * f(n -1); 
}

int main() {
  int n;
  while (~scanf("%d", &n)) {
    printf("f(%d) = %d\n", n, f(n));
  }
  return 0;
}
```

### 斐波那契数列
- 代码示例（斐波那契数列）
```C
#include<stdio.h>
int f(int n) {
  if (n == 1 || n == 2) return 1;
  return f(n -1) + f(n -2);
}
```

### 欧几里得算法
- 算法概要：
```
整数a, b的最大公约数一般表示为 gcd(a, b)
欧几里得算法：gcd(a, b) = gcd(b, a % b)

证明1：b和a%b的最大公约数，是a和b的公约数
证明2：b和a%b的最大公约数，也是a和b的最大公约数
```
- 代码展示
```C
#include<stdio.h>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    int a, b;
    while (scanf("%d%d", &a, &b) != EOF) {
        printf("gcd(%d, %d) = %d\n", a, b, gcd(a, b));
    }

    return 0;
}
```

### 递归函数的设计
- 数据归纳法
  - Step1：验证 P(1) 成立
  - Step2：证明如果 P(K) 成立，那么 P(K+1) 也成立
  - Step3：联合Step1与Step2，证明由P(1) -> P(n) 成立

- 示例：
```
证明：1 + 3 + ... + (2n - 1) = n ^ 2

Step1：
P(1) = 1 = 1 ^ 2  -> P(1) 成立
Step2：
证明n的前一项的奇数和 + 后一项 = n^2
(n - 1) ^ 2 + (2n - 1) = n ^ 2
表达式展开：
公式成立

Step3：
因为Step1成立，同时Step2也成立，所以 Step3成立
```

- 递归函数设计的三个重要部分
  - 重要：给【递归函数】一个明确的语义
  - 实现边界条件时的程序逻辑 -> P(1)
  - 假设递归函数调用返回结果是正确的，实现本层函数逻辑 P(K) -> P(K + 1)

- 重识阶乘
```C
#include<stdio.h>

int f(int n) {             // f(n) 代表 n 的阶乘结果
  if (n == 1) return 1;    // 边界条件：n == 1，即P(1) = 1
  return f(n -1) * n;      // 构造P(K) = P(K + 1)
}
```

### 扩展欧几里得算法
- 贝祖等式：
```
ax + by = gcd(a, b) = c

a, b均为整数，一定存在一组整数解（x,y），使得上述等式成立、

推导过程：(由欧几里得算法推得)
GCD：(a, b) -> (b, a%b) -> ... (c, 0) 即套用到ax = by
则：得到边界条件：x = 1, y = 0
```
- 代码实现
```C
#include<stdio.h>

int x, y, nx, ny;

int ex_gcd(int a, int b) {
    if (b == 0) {
        x = 1, y = 0;
        return a;
    }
    int c = ex_gcd(b, a % b);
    nx = y;
    ny = x - a / b * y;
    x = nx, y = ny;
    return c;
} 


int main() {
    int a, b;
    while (scanf("%d%d", &a, &b) != EOF) {
        int c = ex_gcd(a, b);
        printf("%d * %d + %d * %d = %d\n", a, x, b, y, c);

    }
    return 0;
}
```
### 实战练习-递归实现指数型枚举
- 输出示例
```C
1
1 2
1 2 3
1 3
2
2 3
3
```
- 解题思路
```
1. 明确函数语义：f(i, j, n), i表示数组位置，j表示该位置的最小数字，n表示最大数字，进行遍历枚举

1.2 所以f(i, j, n)的语义是以j为起始的字典序枚举

f(i, j, n)  |  j, f(i + 1, j + 1, n)        ->  | j, j + 1, f (i + 2, j + 2, n)    
            |  j + 1, f(i + 1, j + 2, n)        | j + 2, f(i + 1, j + 3, n)
            |  j + 2, f(i + 1, j + 3, n)        |  ...
            |  ...                              | n, f(i + 1, n + 1, n) 跳出 
            |  n, f(i + 1, n + 1, n) 跳出 
```

- 代码示例
```C

#include<stdio.h>

int arr[10];

// 输出枚举得到的结果
void print_one(int n) {
    for (int i = 0; i <= n; i++) {
        if (i) printf(" ");
        printf("%d", arr[i]);
    }
    printf("\n");
    return ;
}

void f(int i, int j, int n){
    if (j > n) return ;
    for (int k = j; k <= n; k++) {
        // 循环放在这里的意义是重点
        arr[i] = k;
        print_one(i);
        f(i + 1, k + 1, n);
    }
    return ;
}
```
拆分解析1：
```C
void f(int i, int j, int n){
    if (j > n) return ;
    arr[i] = j;
    print_one(i);
    f(i + 1, j + 1, n);
}
// 纯递归
```
输出现象
```C
4
1
1 2
1 2 3
1 2 3 4
```

### 递归实现排列性枚举
```C
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

- 思路
```
1. f(i, n) :从第i位开始，往后枚举n位
2. 又因为，每一位都必须是前面没用过的数字，因此需要一个数组记录使用情况
```

- 代码实现
```C
#include <stdio.h>

int arr[10], vis[10] = {0};

void print_one_res(int n) {
    for (int i = 0; i < n; i++) {
        if (i) printf(" ");
        printf("%d", arr[i]);
    }
    printf("\n");
    return ;
}

void f3(int i, int n) {
    if (i == n) {
        print_one_res(n);
        return ;
    }
    for (int k = 1; k <= n; k++) {
        if (vis[k]) continue;
        arr[i] = k;
        vis[k] = 1;
        f3(i + 1, n);
        vis[k] = 0;
    }
    return ;
}

int main() {
    int n;
    scanf("%d", &n);
    f3(0, n);
    return 0;
}
```

### 递归竞赛题
![Alt text](alg_images/image1.png)
- 解题思路：
```
1. 通过问题将问题分解，简化
1.1 这道题求房屋编号S与D之间得直线距离，实际上就是在求城市等级T中，S和D得坐标，而如果求得S的坐标，同理即可求得D的坐标
1.1.2 因此问题简化为已知城市等级T，求房屋S坐标

2. 观察图形2，图形2是经过图形1，4次变换得到，将图形2分为区域1 - 4
2.1 
区域1为图形等级1 通过顺时针旋转90°，然后轴镜像得到
区域2为图形等级1 通过平移得到
区域3为图形等级1 通过平移得到
区域4为图形等级1 通过逆时针旋转90°，然后轴镜像得到
（注意每个房屋编号的对应关系）
2.2
城市等级2， 可以通过城市等级1的房屋的坐标，经过计算得到城市等级2的各房屋编号对应的坐标
由此推导
城市等级N，可以通过城市等级N-1的房屋坐标，经过计算得到城市等级N的各房屋编号对应的坐标
2.3
完美符合递归的设计结构，城市等级1 - 2为边界条件，城市等级N-1 - N为推导过程，函数可语意明确的用f(T,S) - f(T-1, S)表示，T为城市等级，S为房屋编号

3. 4个区域各自用表达式表示
设在L * L 的矩阵中，（x, y）在区域1（即顺时针旋转90°，然后轴镜像得到）
旋转：(x, y) -> (y, L - 1 - x) 再镜像：(y, L - 1 - x) -> (y, x)
区域2：(x, y) -> (x, y + L)
区域3：(x, y) -> (x + 2, y + L)
区域4：(x, y) -> (n - 1 - y, x) -> (2L - 1 - y, L - x - 1)
(区域4，逆时针旋转90，然后轴镜像，然后向下平移)

```

- 完整代码
```C
#include<stdio.h>
#include<math.h>
#define S(a) ((a) * (a))

void f(long long  n, long long s, long long *x, long long *y) {
    if (n == 1) {
        if (s == 1) *x = 0, *y = 0;
        else if (s == 2) *x = 0, *y = 1;
        else if (s == 3) *x = 1, *y = 1;
        else *x = 1, *y = 0;
        return ;
    }
    long long L = pow(2LL, n - 1);
    long long block = L * L; // 点的数量
    long long xx, yy;
    if (s <= block){
        // 1号区域
        f(n - 1, s, &xx, &yy);
        *x = yy, *y = xx;
    } else if (s <= 2 * block) {
        // 2号区域
        f(n - 1, s - block, &xx, &yy);
        *x = xx, *y = yy + L;
    } else if (s <= 3 * block) {
        // 3号区域
        f(n - 1, s - 2 * block, &xx, &yy);
        *x = xx + L, *y = yy + L;
    } else {
        // 4号区域
        f(n - 1, s - 3 * block, &xx, &yy);
        *x = 2 * L - yy - 1, *y = L - xx - 1;
    }
    return ;
}

int main() {
    long long t, n, s, d;
    scanf("%lld", &t);
    while (t--) {
        scanf("%lld%lld%lld", &n, &s, &d);
        long long  sx, sy, dx, dy;
        f(n, s, &sx, &sy);
        f(n, d, &dx, &dy);
        printf("%.0lf\n", 10 * sqrt(S(sx - dx) + S(sy - dy)));
    }
    return 0;
}
```



