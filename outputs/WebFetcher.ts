import axios from 'axios';

interface IWebFetcher {
  fetch(url: string): Promise<string>;
}

class WebFetcher implements IWebFetcher {
  async fetch(url: string): Promise<string> {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);
    const header = $('header').html();
    const footer = $('footer').html();
    return `${header}\n${footer}`;
  }
}

export { WebFetcher, IWebFetcher };