### Class 9: Web Scraping and Data Cleansing
* Pandas homework with the IMDb data due ([solution](homework solutions/05_pandas_homework_imdb.py))
* Web scraping ([code](code/09_web_scraping.py))
    * [IMDb: robots.txt](http://www.imdb.com/robots.txt)
    * [Example web page](data/example.html)
    * [IMDb: The Shawshank Redemption](http://www.imdb.com/title/tt0111161/)
    * [Be Suspicious Of Online Movie Ratings, Especially Fandangos](http://fivethirtyeight.com/features/fandango-movies-ratings/)
* APIs ([code](code/09_api.py))

**Homework:**
* **Optional:** Complete the homework exercise listed in the [web scraping code](code/07_web_scraping.py). It will take the place of any one homework you miss, past or future!

**Web Scraping Resources:**
* The [Beautiful Soup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is incredibly thorough, but is hard to use as a reference guide. However, the section on [specifying a parser](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) may be helpful if Beautiful Soup appears to be parsing a page incorrectly.
* For more Beautiful Soup examples and tutorials, see [Web Scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/), this [notebook](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html) from Stanford's Text As Data course, and this [notebook](https://github.com/cs109/2014/blob/master/lectures/2014_09_23-lecture/data_scraping_transcript.ipynb) and associated [video](http://cm.dce.harvard.edu/2015/01/14328/L07/screen_H264LargeTalkingHead-16x9.shtml) from Harvard's Data Science course.
* For a much longer web scraping tutorial covering Beautiful Soup, lxml, XPath, and Selenium, watch [Web Scraping with Python](https://www.youtube.com/watch?v=p1iX0uxM1w8) (3 hours 23 minutes) from PyCon 2014. The [slides](https://docs.google.com/presentation/d/1uHM_esB13VuSf7O1ScGueisnrtu-6usGFD3fs4z5YCE/edit#slide=id.p) and [code](https://github.com/kjam/python-web-scraping-tutorial) are also available.
* For more complex web scraping projects, [Scrapy](http://scrapy.org/) is a popular application framework that works with Python. It has excellent [documentation](http://doc.scrapy.org/en/1.0/index.html), and here's a [tutorial](https://github.com/rdempsey/ddl-data-wrangling) with detailed slides and code.
* [robotstxt.org](http://www.robotstxt.org/robotstxt.html) has a concise explanation of how to write (and read) the `robots.txt` file.
* [import.io](https://import.io/) and [Kimono](https://www.kimonolabs.com/) claim to allow you to scrape websites without writing any code.
* [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) and [How Netflix Reverse Engineered Hollywood](http://www.theatlantic.com/technology/archive/2014/01/how-netflix-reverse-engineered-hollywood/282679/?single_page=true) are two fun examples of how web scraping has been used to build interesting datasets.

**API Resources:**
* This Python script to [query the U.S. Census API](https://github.com/laurakurup/census-api) was created by a former DAT student. It's a bit more complicated than the example we used in class, it's very well commented, and it may provide a useful framework for writing your own code to query APIs.
* [Mashape](https://www.mashape.com/explore) and [Apigee](https://apigee.com/providers) allow you to explore tons of different APIs. Alternatively, a [Python API wrapper](http://www.pythonforbeginners.com/api/list-of-python-apis) is available for many popular APIs.
* The [Data Science Toolkit](http://www.datasciencetoolkit.org/) is a collection of location-based and text-related APIs.
* [API Integration in Python](https://realpython.com/blog/python/api-integration-in-python/) provides a very readable introduction to REST APIs.
* Microsoft's [Face Detection API](https://www.projectoxford.ai/demo/face#detection), which powers [How-Old.net](http://how-old.net/), is a great example of how a machine learning API can be leveraged to produce a compelling web application.

-----

### Class 10: Basic Model Evaluation
* Reproducibility
    * Discuss assigned readings: [introduction](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/), [Colbert Report video](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error), [cabs article](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2), [Tweet](https://twitter.com/jakevdp/status/519563939177197571), [creating a reproducible analysis](https://github.com/jtleek/datasharing)
    * Examples: [Classic rock](https://github.com/fivethirtyeight/data/tree/master/classic-rock), [student project 1](https://github.com/jwknobloch/DAT4_final_project), [student project 2](https://github.com/justmarkham/DAT4-students/tree/master/Jonathan_Bryan/Project_Files)
* Discuss the reading assignment on the [bias-variance tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html)
* Model evaluation using train/test split ([notebook](notebooks/10_model_evaluation.ipynb))
* Exploring the scikit-learn documentation: [module reference](http://scikit-learn.org/stable/modules/classes.html), [user guide](http://scikit-learn.org/stable/user_guide.html), class and function documentation

**Homework:**
* Watch Rahul Patwari's videos on [probability](https://www.youtube.com/watch?v=o4QmoNfW3bI) (5 minutes) and [odds](https://www.youtube.com/watch?v=GxbXQjX7fC0) (8 minutes) if you're not comfortable with either of those terms.
* Read these excellent articles from BetterExplained: [An Intuitive Guide To Exponential Functions & e](http://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/) and [Demystifying the Natural Logarithm (ln)](http://betterexplained.com/articles/demystifying-the-natural-logarithm-ln/). 

**Model Evaluation Resources:**
* For a recap of some of the key points from today's lesson, watch [Comparing machine learning models in scikit-learn](https://www.youtube.com/watch?v=0pP4EwWJgIU) (27 minutes).
* For another explanation of training error versus testing error, the bias-variance tradeoff, and train/test split (also known as the "validation set approach"), watch Hastie and Tibshirani's video on [estimating prediction error](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34).
* Caltech's Learning From Data course includes a fantastic video on [visualizing bias and variance](http://work.caltech.edu/library/081.html) (15 minutes).
* [Random Test/Train Split is Not Always Enough](http://www.win-vector.com/blog/2015/01/random-testtrain-split-is-not-always-enough/) explains why random train/test split may not be a suitable model evaluation procedure if your data has a significant time element.

**Reproducibility Resources:**
* [Software development skills for data scientists](http://treycausey.com/software_dev_skills.html) discusses the importance of writing functions and proper code comments (among other skills), which are highly useful for creating a reproducible analysis.
* [Data science done well looks easy - and that is a big problem for data scientists](http://simplystatistics.org/2015/03/17/data-science-done-well-looks-easy-and-that-is-a-big-problem-for-data-scientists/) explains how a reproducible analysis demonstrates all of the work that goes into proper data science.

-----

### Class 11: Logistic Regression
* Optional web scraping homework due ([solution](homework solutions/07_web_scraping.py))
* Logistic regression ([notebook](notebooks/12_logistic_regression.ipynb))
    * [Glass identification dataset](https://archive.ics.uci.edu/ml/datasets/Glass+Identification)
* Exercise with Titanic data ([notebook](notebooks/12_titanic_confusion.ipynb), [data](data/titanic.csv), [data dictionary](https://www.kaggle.com/c/titanic/data))
* Confusion matrix ([slides](slides/12_confusion_matrix.pdf), [notebook](notebooks/12_titanic_confusion.ipynb))

**Homework:**
* If you aren't yet comfortable with all of the confusion matrix terminology, watch Rahul Patwari's videos on [Intuitive sensitivity and specificity](https://www.youtube.com/watch?v=U4_3fditnWg) (9 minutes) and [The tradeoff between sensitivity and specificity](https://www.youtube.com/watch?v=vtYDyGGeQyo) (13 minutes).

**Logistic Regression Resources:**
* To go deeper into logistic regression, read the first three sections of Chapter 4 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), or watch the [first three videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) (30 minutes) from that chapter.
* For a math-ier explanation of logistic regression, watch the first seven videos (71 minutes) from week 3 of Andrew Ng's [machine learning course](https://www.coursera.org/learn/machine-learning/home/info), or read the [related lecture notes](http://www.holehouse.org/mlclass/06_Logistic_Regression.html) compiled by a student.
* For more on interpreting logistic regression coefficients, read this excellent [guide](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm) by UCLA's IDRE and these [lecture notes](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf) from the University of New Mexico.
* The scikit-learn documentation has a nice [explanation](http://scikit-learn.org/stable/modules/calibration.html) of what it means for a predicted probability to be calibrated.
* [Supervised learning superstitions cheat sheet](http://ryancompton.net/assets/ml_cheat_sheet/supervised_learning.html) is a very nice comparison of four classifiers we cover in the course (logistic regression, decision trees, KNN, Naive Bayes) and one classifier we do not cover (Support Vector Machines).

**Confusion Matrix Resources:**
* [simple guide to confusion matrix terminology](http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) may be useful to you as a reference.
* This blog post about [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/amazon-machine-learning-make-data-driven-decisions-at-scale/) contains a neat [graphic](https://media.amazonwebservices.com/blog/2015/ml_adjust_model_1.png) showing how classification threshold affects different evaluation metrics.
* This notebook (from another DAT course) explains [how to calculate "expected value"](https://github.com/podopie/DAT18NYC/blob/master/classes/13-expected_value_cost_benefit_analysis.ipynb) from a confusion matrix by treating it as a cost-benefit matrix.

-----

### Class 12: Advanced Model Evaluation
* Cross-validation
    * Discuss cross-validation [notebook](notebooks/13_cross_validation.ipynb)
* Data preparation ([notebook](notebooks/13_advanced_model_evaluation.ipynb))
    * Handling missing values
    * Handling categorical features (review)
* ROC curves and AUC
    * Discuss the [video/reading assignment](homework/13_roc_auc.md)
    * Exercise: drawing an ROC curve ([slides](slides/13_drawing_roc.pdf))
    * Return to the main notebook
* Exercise with bank marketing data ([notebook](notebooks/13_bank_exercise.ipynb), [data](data/bank-additional.csv), [data dictionary](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing))

**Homework:**
* Your first project presentation is on Tuesday (11/2)! Please submit a link to your project repository (with slides) by 6pm on Tuesday.
* Complete the [homework assignment](homework/10_yelp_votes.md) with the [Yelp data](data/yelp.csv). This is due on Thursday (11/4).
* Reading assignment on [spam filtering](homework/14_spam_filtering.md)
* Read these [Introduction to Probability](https://docs.google.com/presentation/d/1cM2dVbJgTWMkHoVNmYlB9df6P2H8BrjaqAcZTaLe9dA/edit#slide=id.gfc3caad2_00) slides, or skim section 2.1 of the [OpenIntro Statistics textbook](https://www.openintro.org/stat/textbook.php?stat_book=os) (12 pages). Pay specific attention to the following terms: probability, mutually exclusive, sample space, independent.
* **Optional:** Try to gain an understanding of conditional probability from this [visualization](http://setosa.io/conditional/).
* **Optional:** For an intuitive introduction to Bayes' theorem, read these posts on [wealth and happiness](http://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule/answer/Michael-Hochster), [ducks](https://planspacedotorg.wordpress.com/2014/02/23/bayes-rule-for-ducks/), or [legos](http://www.countbayesie.com/blog/2015/2/18/bayes-theorem-with-lego).

**ROC Resources:**
* Rahul Patwari has a great video on [ROC Curves](https://www.youtube.com/watch?v=21Igj5Pr6u4) (12 minutes).
* [An introduction to ROC analysis](http://people.inf.elte.hu/kiss/13dwhdm/roc.pdf) is a very readable paper on the topic.
* ROC curves can be used across a wide variety of applications, such as [comparing different feature sets](http://research.microsoft.com/pubs/205472/aisec10-leontjeva.pdf) for detecting fraudulent Skype users, and [comparing different classifiers](http://www.cse.ust.hk/nevinZhangGroup/readings/yi/Bradley_PR97.pdf) on a number of popular datasets.

**Cross-Validation Resources:**
* For more on cross-validation, read section 5.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (11 pages) or watch the related videos: [K-fold and leave-one-out cross-validation](https://www.youtube.com/watch?v=nZAM5OXrktY) (14 minutes), [cross-validation the right and wrong ways](https://www.youtube.com/watch?v=S06JpVoNaA0) (10 minutes).
* If you want to understand the different variations of cross-validation, this [paper](http://www.jcheminf.com/content/pdf/1758-2946-6-10.pdf) examines and compares them in detail.
* To learn how to use [GridSearchCV and RandomizedSearchCV](http://scikit-learn.org/stable/modules/grid_search.html) for parameter tuning, watch [How to find the best model parameters in scikit-learn](https://www.youtube.com/watch?v=Gol_qOgRqfA) (28 minutes) or read the [associated notebook](https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb).

**Other Resources:**
* scikit-learn has extensive documentation on [model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html).
* [Counterfactual evaluation of machine learning models](https://www.youtube.com/watch?v=QWCSxAKR-h0) (45 minutes) is an excellent talk about the sophisticated way in which Stripe evaluates its fraud detection model. (These are the associated [slides](http://www.slideshare.net/MichaelManapat/counterfactual-evaluation-of-machine-learning-models).)

-----

## Meet the Team
### Mahmoud Lababidi (Instructor)
Mahmoud is a Data Scientist and Engineer at HumanGeo, a local Government Contractor. 
He has a varied set of experiences in the data science realm in technologies from Machine Learning to data analysis. 
He spent many years earning a doctorate in physics and enjoys long walks on the beach doing quantum physics. 
He is an avid wannabe audiophile and enjoys the DC music scene.

**Contact Info:**
* Email: [lababidi@gmail.com](mailto:lababidi@gmail.com)

### Alex Sherman (Associate Instructor)
Alex is a passionate business analytics advocate. He currently works as a Technology Consultant at Deloitte Consulting, 
in which he leads the design and implementation for informatics and analytics software development projects, 
repurposing semantic open source software to enhance data access for federal health care clients. 
In his free time, Alex is an avid jazz percussionist, self-proclaimed as the best drum stick spinner in the DC metro area.

**Contact Info:**
* Email: [alexjmsherman@gmail.com](mailto:alexjmsherman@gmail.com)

### Tim Foley (Course Producer)
As your Course Producer, it's Tim's job to make sure that you (and your instructors) have everything you need for a successful experience in DAT9. **If you've got a question, and you're not sure who to ask, start with Tim!**

Before GA, Tim lived and worked in China as a facilitator and program-designer for youth leadership programs at international schools all over Asia (e.g. student-council retreats, backpacking trips, etc.). After a year abroad, he was ready to move back to the good ol' USA. Tim started out at the front desk as a member of GA's Front Lines team, moved up to "Campus Commander" (yes, a real title), and then in January started as a full-time Course Producer. In addition to Data Science, Tim also produces Front- and Back-End Web Development, Data Analytics, Mobile Development, and Digital Marketing. Tim has been trying to learn Esperanto since high school.

**Contact Info**
* Email: [tim.foley@generalassemb.ly](mailto:tim.foley@generalassemb.ly)
* Phone: 202-748-3694
* and Slack too!
