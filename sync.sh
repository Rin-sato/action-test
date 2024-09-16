#!/usr/bin/expect
set timeout 20
spawn mount -t davfs https://wp.hapuren.cn/123pan/user1-1/ mirrors/
expect "Username:"
send "twentyone\r"
expect "Password:"
send "twentyone\r"
expect eof