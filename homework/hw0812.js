alert( "你好，我是外部javascript（唉，不想用print函数）")
let q1 = prompt("作业做的怎么样?好的话，输入yes,不好的话，输入no");
while (true) {
    if (q1 == "yes") {
        alert("谢谢鼓励，我会继续努力的");
        break;
    } else if (q1 == "no") {
        alert("……，想找个阿姨躺平了，不想努力了");
        break;
    } else {
        alert("你输入的不对，请重新输入，注意大小写");
        q1 = prompt("作业做的怎么样?好的话，输入yes,不好的话，输入no");
    } 

} 
alert("再次查看请刷新网页");