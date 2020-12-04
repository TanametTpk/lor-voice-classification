# Usages
- install node
- npm i
- node main.js
- access to http://localhost:8081
- press start
- enjoy!!!

# Commands
## Select Card
- ["เลือกไพ่ใบที่", "เลือกใบที่", "เลือกไพ่ที่", "เอาไพ่ที่", "เอาไพ่ใบที่", "เอาไพ่ที่", "เอาใบที่", "ไพ่ที่", "ใบที่"] n
- เช่น เลือกไพ่ใบที่ 3

## Use Card
- ["ลง", "ใช้"]
- ใช้คู่กับ command อื่นๆ
- เช่น เอาไพ่ที่ 2 ลง

## Select Character
- ["เลือกตัวที่", "เอาตัวที่"] n
    - ["โจมตี", "ตี", "attack"]
    - ["ป้องกัน", "กัน", "block"] ตัวที่ m
- ป้องกัน เช่น เลือกตัวที่ 2 กัน ตัวที่ 1
- โจมตี เช่น เลือกตัวที่ 3 โจมตี

## Attack All
- ["โจมตีทั้งหมด", "ตีทั้งหมด", "direct attack"]

## End Turn
- ["จบ", "skip", "ข้าม", "ผ่าน"]

## Sequence Example
- ไบที่ 1 ใช้ ตีทั้งหมด ผ่าน

# Limitation
- local model voice recognition ที่ใช้เป็น api ของ chrome จึงใช้ได้แค่ browser สกุล chrome เท่านั้น
- main language ใช้เป็นภาษาไทย การพูดศัพท์ Eng จะติดยากหน่อย และ ใช้ Eng สำเนียงไทย จะดีที่สุด