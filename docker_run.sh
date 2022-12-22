# You need to change the path to the config folder to match your machine
docker run --name flat-finder -v /Users/philippbergmann/repos/flat-finder/config/:/conf phil-bgm/flat-finder
docker start flat-finder