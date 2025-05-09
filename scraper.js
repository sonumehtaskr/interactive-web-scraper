const axios = require('axios');
const cheerio = require('cheerio');

async function scrapeTitles(url, tag = 'h2', className = '') {
  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);
    console.log($,data)
    const elements = className ? $(tag + '.' + className) : $(tag);
    return elements.map((i, el) => $(el).text().trim()).get();
  } catch (error) {
    return [`Error: ${error.message}`];
  }
}

module.exports = scrapeTitles;
