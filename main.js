const express = require('express')
const path = require('path')
const controller = require('./interfaces/controller')

const port = 8081

const app = express()
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use(express.static(path.join(__dirname, 'public')))

app.get('/', (req, res) => {
    res.render('teach')
})

app.post('/actions', (req, res) => {
    console.log(req.body);
    let {label} = req.body

    controller.exec(label)
    res.status(200).send()
})

app.listen(port, () => {
    console.log("listen on port", port);
})
