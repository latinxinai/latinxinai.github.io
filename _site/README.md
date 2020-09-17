# LatinX in AI Coalition

![](./assets/img/particle.jpg)

This is an opensource website for LatinX in AI (LXAI). Our organization is volunteer run, so we welcome and encourage contributions from our community and allies! 

Familiarize yourself with the following documentation before getting started.

## The Docs:

- [Github Pages Hosting](https://pages.github.com/)
- [Jekyll Site Generator](https://jekyllrb.com/)
- [Particle Jekyll Theme](https://jekyll-themes.com/particle/)
- [NodeJS](https://nodejs.org/)
- [NPM](https://www.npmjs.com/get-npm)
- [Yarn](https://yarnpkg.com/en/)
- [Particle.js](https://github.com/VincentGarreau/particles.js/)
- [Google Analytics](https://analytics.google.com/analytics/web/provision/?authuser=0#/provision)
- [Open-Source Style Guides](http://google.github.io/styleguide/)

## Basic Setup

To contribute to this opensource website, complete the following steps:

1. Clone this repository.
    `git clone https://github.com/latinxinai/latinxinai.github.io.git`
2. Change directories into cloned repository.
    `cd latinxinai.github.io`
2. Create your own branch.
    `git checkout -b 'your-branch-name'`
3. Install [Ruby](https://www.ruby-lang.org/en/downloads/) and [Jekyll](https://jekyllrb.com/docs/installation/) if you haven't already.
4. Install [Node.js](https://nodejs.org/) and NPM is you haven't already.
3. Install node packages 
    `npm install`


## Running Locally

In order to compile the assets and run the latest version of the site locally complete the following:

- Pull latest version
    `git pull origin master`
- Run Jekyll Server
    `jekyll serve`
- Now browse to http://localhost:4000


## File Structure
This site follows the general structure of a [jekyll](https://jekyllrb.com/docs/structure/) github pages site.

For changes to workshop pages, please only edit the following:
1. [_pages](/_pages/)
    - There should be a separate workshop site directory for each conference we colocate with identified by the acronym and year, ex: XXXX_YYYY
    - Each workshop site directory should contain at minimum the following pages
        - home page
        - sponsor page
        - schedule page
        - presenter page
    - Each of these pages should include the corresponding nav and footer files
    - Duplicate of each page should be made available in Spanish and Portugese if possible
    - Use previous years workshops as a template for creating new pages

2. [_includes](/_includes/)
    - Directories organized by conference acronym then year of conference, ex: XXXX/YYYY/
    - This is where the content for all pages will be created and modified
    - At minimum there should be created and maintained the following includes files:
        - about 
            - contains the information displayed on the homepage of the workshop website
        - header
            - navbar on the homepage of the workshop website
        - header alt
            - navbar on all alternative pages of the workshop website
        - presenters
            - lists the selected presenters with additional information
        - schedule
            - lists the final schedule of the day
        - sponsor
            -  sponsorship deck with levels, etc

3. [_posts](/_posts/)
    - This directory is where the data for each presenter is stored
    - keep organized by year and conference we are colocating with, ex: YYYY_XXXX_speakers
    - Use previous years as a template for creating new presenter data files


**All the code is compiled into the _site directory and served during build by jekyll from the master branch. If you make manual changes to code in the _site directory they will be overwritten automatically.**


## Pushing Changes

Follow these **guidelines** when contributing to this site:

- Always work off your own branch!
- Never push to the master branch!!
- Push to your branch and then [create a pull request](https://help.github.com/articles/creating-a-pull-request/).
- Follow standard [open-source style guides](http://google.github.io/styleguide/).
- Correct any suggested edits from LXAI and resubmit your pull request for additional review.
- Once your changes have been accepted and merged to master by a representative of the LatinX in AI (LXAI), your name may be added to the credits below. 


## Questions

Having any issues with the site? See something that can be improved? 

File a [GitHub Issue](https://github.com/latinxinai/latinxinai.github.io/issues).										

## License

GNU General Public License v3.0

## Credits

This theme was partially designed with the inspiration from these fine folks
- [Willian Justen](https://github.com/willianjusten/will-jekyll-template)
- [Vincent Garreau](https://github.com/VincentGarreau/particles.js/)
- [Nathan Randecker](https://github.com/nrandecker/)

This site has been modified by and built upon by the these folks
- [Laura Montoya](https://github.com/quickresolve)
- [Pablo Samuel Castro](https://github.com/psc-g)
- [Yannet Interian](https://github.com/yanneta)
- [Sebastian Anaya](https://github.com/seby408)
- [Victor Ramirez](https://github.com/vhr1975)
- [Pablo Rivas](https://github.com/pablorp80)
- [Maria Pantoja](https://github.com/mpantoja314)
- [Juan Camilo](https://github.com/juancamilog)
- [Kevin Bello](https://github.com/kevinsbello)
- [Walter Mayor](https://github.com/waltermayor)
- [Josue Ortega Caro](https://github.com/josueortc)
- [Gissella Bejarano](https://github.com/gissemari)