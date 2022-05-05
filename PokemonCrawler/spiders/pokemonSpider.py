import scrapy
import os


PATH = '/Users/TheoV22/PokemonCrawler/PokemonCrawler/CSV/'


class PokemonSpider(scrapy.Spider):

    name = 'pokemon_spider'
    custom_settings = {
        'FEEDS': {PATH + 'pokemonResults.csv': {'format': 'csv'}}
    }
    start_urls = []
    for x in range(1, 152):
        x = str(x).zfill(3)
        i = f'https://www.serebii.net/pokedex-rs/{x}.shtml'
        start_urls.append(i)
    
    try:
        os.remove(PATH + 'pokemonResults.csv')
    except OSError:
        pass

    def parse(self, response): 


        yield {
            # Sometimes, we have to remove all the 'tbody' in the xpath, otherwise it won't works.
            # We have to add the '//text()' to get only the text line.
            'name':response.xpath('//*[@id="content"]/main/div/table[4]/tr[2]/td[4]//text()').extract(),
            'attack1': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[1]/td[2]/a//text()').extract(),
            'attack2': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[3]/td[2]/a//text()').extract(),
            'attack3': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[5]/td[2]/a//text()').extract(),
            'attack4': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[7]/td[2]/a//text()').extract(),
            'attack5': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[9]/td[2]/a//text()').extract(),
            'attack6': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[11]/td[2]/a//text()').extract(),
            'attack7': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[13]/td[2]/a//text()').extract(),
            'attack8': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[15]/td[2]/a//text()').extract(),
            'attack9': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[17]/td[2]/a//text()').extract(),
            'attack10': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[19]/td[2]/a//text()').extract(),
            'attack11': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[21]/td[2]/a//text()').extract(),
            'attack12': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[23]/td[2]/a//text()').extract(),
            'attack13': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[25]/td[2]/a//text()').extract(),
            'attack14': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[27]/td[2]/a//text()').extract(),
            'attack15': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[29]/td[2]/a//text()').extract(),
            'attack16': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[31]/td[2]/a//text()').extract(),
            'attack17': response.xpath('//*[@id="content"]/main/div/table[10]/tbody/tr[33]/td[2]/a//text()').extract(),            
        }
