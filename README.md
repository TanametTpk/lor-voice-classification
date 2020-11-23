# Usages
- install node
- npm i
- node main.js
- access to http://localhost:8081
- press start
- enjoy!!!

# Configs
- I hope you can write javascript 555.
- you can change action in interfaces/controller.js
- you can change model in views/teach.ejs
   - at URL = http://localhost:8081/<model_name>/
      - clap
         - clap for attack all
         - snap for end turn
      - largemodels
         - more sensitive with other label
      - models
         - less sensitive with other label
- you can train you model easily with https://teachablemachine.withgoogle.com/
   - select Audio Project
   - add your class
   - train
   - export and download as tensorflow.js to local
   - extract to public folder
   - change views/teach.ejs
   - (optional) custom labels change in controller.js