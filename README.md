# flat-finder

Looking for a flat can be a very time consuming process, especially in a big city in Germany. To facilitate that for myself I created this small bot and wanted to share the code here if someone else might find it useful. Consider this project work in progress and I'm not planning to mantain it for a long time, although it already runs since 3 weeks without a problem for myself.

## Usage
First you need to go to the `./config` folder and copy the `.env.example` to `.env`. Now edit the `.env` file according to your needs. The entries should be self explanatory, but some more notes here:
* You can use multiple notification channels at once or only one of them. But deactivate the ones where you do not provide credentials.
* In this folder there will automatically be placed a file called `sent_flats.txt` to keep track which flats were sent to the notification channels. When both channels are active a success is when the bot was able to send it to at least one channel. To reset the bot and send all flats again just delete this file.
* You can change the URL parameter whenever you want, the `sent_flats.txt` will still be reused.
* If you want to use immoscout you will need to create a [scrapingbee](https://www.scrapingbee.com/) account and place the credentials in the file as they have some serious bot protection on their page. This was the only provider I found that worked and it will use the most expensive option (I think it was 75 credits per call) from this service. So to use it you will need to upgrade to the paid version very soon (that unfortunately costs around 50€ per month). Especially when using this service adapt `REFRESH_EVERY_MINUTES` and `RETRIES` fields.
* For new config parameters to be used restart the bot.

Now go to the parent folder of this repos and build the docker container:
```sh
docker build -t phil-bgm/flat-finder .
```

Then you can start the container with (replace `/Users/philippbergmann/repos/flat-finder/config/` with the path to your `config` folder):
```sh
docker run -d --name flat-finder -v /Users/philippbergmann/repos/flat-finder/config/:/conf phil-bgm/flat-finder
```

It is a good idea to check the logs from time to time (especially in the beginning):
```sh
docker logs flat-finder
```

## Inspirations
This project is heavily inspired by:
* [Fredy](https://github.com/orangecoding/fredy)
