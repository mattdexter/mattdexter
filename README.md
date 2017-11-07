# Dockerized Django server
This is the server that hosts my Django apps.

Enter your environment variables in .env.smpl and rename it to .env, then run with

    source .env && docker-compose up -d

Pull apps from my other repos entitled mattdexter-\[appname\], into ./webapp, e.g.:

    git clone git@github.com:mattdexter/mattdexter-portfolio ./webapp/portfolio && docker-compose restart

Then open a shell in the webapp container and perform necessary database migrations, data loading, etc. with Django.