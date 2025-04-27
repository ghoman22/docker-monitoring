const express = require('express')
const fs = require('fs')
const path = require('path')
const client = require('prom-client')

const app = express()

app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, 'views'))

// 🎯 Buat metric baru: http_requests_total dengan label 'method' dan 'path'
const register = new client.Registry()
const httpRequestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'path']
})
client.collectDefaultMetrics({ register })
register.registerMetric(httpRequestCounter)

// 🖥️ Setiap route perlu menghitung request-nya
app.get('/', (req, res) => {
  httpRequestCounter.inc({ method: req.method, path: req.path })  // Tambahkan label 'method' dan 'path'
  res.render('index')
})

app.get('/log', (req, res) => {
  httpRequestCounter.inc({ method: req.method, path: req.path })  // Tambahkan label 'method' dan 'path'
  fs.appendFileSync('log.txt', `Log at ${new Date().toISOString()}\n`)
  res.send("Log written")
})

app.get('/slow', (req, res) => {
  httpRequestCounter.inc({ method: req.method, path: req.path })  // Tambahkan label 'method' dan 'path'
  setTimeout(() => {
    res.send("Delayed response done!")
  }, 3000)
})

app.get('/read', (req, res) => {
  httpRequestCounter.inc({ method: req.method, path: req.path })  // Tambahkan label 'method' dan 'path'
  const content = fs.existsSync('log.txt') ? fs.readFileSync('log.txt', 'utf-8') : 'No log found.'
  res.send(`<pre>${content}</pre>`)
})

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType)
  res.end(await register.metrics())
})

app.listen(3000, () => console.log('Running on port 3000'))
