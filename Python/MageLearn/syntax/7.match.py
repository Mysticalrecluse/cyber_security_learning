# match语句

# match语句是Python3.10中引入的新特性，用于替代复杂的if-elif-else语句。
http_response_status = 404

match http_response_status:
    case 400:
      print("Bad request")
    case 404:
      print("No found") # match语句会自动终止，不会继续匹配其他模式
    case 418:
      print("i'm a teapot")
    case _:
      print("Something's wrong with the internet")
      #变量名“_”为通用匹配符，确保match必定被匹配成功。

# match语句组合模式
match http_response_status:
    case 400|403|404: #可以使用“|”在一个模式中组合多个字面值
      print("4XX error")
    case 500|501|503:
      print("5XX error")
    case _:
      print("strange wrong")

