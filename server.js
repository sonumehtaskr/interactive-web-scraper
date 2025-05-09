const express = require('express');
const scrapeTitles = require('./scraper');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('index', { results: null });
});

app.post('/scrape', async (req, res) => {
  const { url, tag, className } = req.body;
  console.log('body',req.body)
  const results = await scrapeTitles(url, tag || 'h2', className || '');
  res.render('index', { results });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
