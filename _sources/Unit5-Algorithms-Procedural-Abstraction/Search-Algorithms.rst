.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Search Algorithms
=================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['5.03']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit5-Algorithms-Procedural-Abstraction/Search-Algorithms.html" target="_blank" title="">This lesson</a> introduces one common group of algorithms: searches. Through a number guessing game, students explore the efficiency of binary and sequential search algorithms as well as write the pseudocode for binary search.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit5-Algorithms-Procedural-Abstraction/Search-Algorithms.html" target="_blank" title="">Unit 5 Lesson 5.3: Search Algorithms</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Computer lab with projection system</li><li><a href="https://youtu.be/0eKVizvYSUQ" target="_blank" title="">Video: How Google Search Works</a></li><li><a href="https://mobile-csp.org/webapps/search/binarygame.html" target="_blank" title="">Binary Game</a> (without feedback)</li><li><span class="yui-non"><a href="https://mobile-csp.org/webapps/search/binary.html" target="_blank" title="">Binary Game</a> with too high/too low feedback</span></li><li><a href="https://docs.google.com/document/d/1HQCHw9qhIq5M7a57xjMn-daD7BdVv7h3fjA4J8Vn160/edit" target="_blank" title="">POGIL Worksheet</a></li><li><a href="https://docs.google.com/document/d/1_NfNLWJxaG4qZ2Jd2x8UctDS05twn1h6p-o3XaAcRv0/edit" target="_blank" title="">POGIL Roles</a></li><li><a href="https://mobile-csp.org/webapps/search/sequential.html" target="_blank" title="">Linear/Sequential Search Game</a></li><li><a href="https://docs.google.com/presentation/d/1HnDhg9zF2_kEgWY10yx6ZebLdS89GYQJwofzqCqhn74/" target="_blank" title="">Slides by Mobile CSP Teacher Mary Rucker</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (10 minutes):</b> Bring a phonebook or dictionary to class and ask a student look up something in the middle of the alphabet like "lawyer". The student will predictably open the book in the middle using a version of binary search. Ask the other students why didn't the student start at page 1? Ask students to think about how Google is able to search web pages for things like "cat videos" or your name. Show the video on "How Search Works"</li>
    <li><b>Experiences and Explorations (30 minutes):</b>
    <ul>
    <li><b>Guessing Game:</b> In pairs, have one student select a secret number between 1 and 100. The other student should try to guess it with as few guesses as possible. Students can let them know if guesses are too high or too low...or correct! Have them switch and repeat the process. Share strategies as a class for guessing the number.
          </li>
    <li><b>Explanation:</b> Explain that the students have just used a <b><i>binary search strategy</i></b> — guessing in the middle to rule out either the top or bottom half of numbers. This is an efficient strategy because half of the remaining numbers are able to be eliminated with each guess. Now ask students what they think would be the worst strategy for guessing in that it would take the most number of guesses. Hopefully, someone suggests <b><i>sequential (linear) search</i></b> — one in which you guess every number starting at one, all the way up to 100.</li>
    <li><b>POGIL Activity:</b> Divide students into POGIL groups and have them choose roles. Students should work together to answer the questions about binary search, using the widget or by hand. When finished, they should review the widget for sequential search as well.</li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> In pairs, have the students write a paragraph giving directions for a sequential search and for a binary search. Share the paragraphs with the class and check for missing details. Have the students complete the interactive exercises and their portfolio reflections.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    <ul>
    <li>Topic 3.11 Binary Search</li>
    </ul>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <p><b>Solutions</b> 
    <i>Note: Solutions are only available to verified educators who have joined the <a href="../Unit1-Getting-Started/PD-Joining-the-Forum.html" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</i></p>
    <b>POGIL Solutions:</b><br/>
    <ul>
    <li>Here is the guessing game <a href="http://appinventor.trincoll.edu/csp/webapps/search/binarysearch.html" target="_blank">pseudocode</a> and an explanation of how binary search works.</li>
    <li>
          To guess a number between 1 and 100, the maximum number of guesses the algorithm would take is 7 because 100 can be divided into two 7 times before ending up with just 1 number: 100/2 = 50/2 = 25/2 = 13/2 = 7/2 = 4/2 = 2/2 = 1. Or you could compute log<sub>2</sub> 100 = 7 (rounded up). You could also 2<sup>7</sup> = 128 and 2<sup>6</sup> is 64 so to get through 100 numbers by repeatedly halving, it would take at most 7 steps.</li>
    <li> To guess a number between 1 and 500,  the maximum number of guesses the  algorithm would take is 9 since 2<sup>9</sup> is 512 or log<sub>2</sub> 500 = 9. If you repeatedly halve 500 numbers, you would need at most 9 steps to get to 1 number: 500/2 = 250/2 = 125/2 = 63/2 = 32/2 = 16/2 = 8/2 = 4/2 = 2/2 = 1</li>
    </ul>
    <b>    Other Solutions:</b> <br/>
    <ul>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/umn.edu/mobilecspportfolioanswerkey/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p><b>Assessment Opportunities</b></p>
    <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.</p>
    <ul>
    <li><i><b>Interactive Exercises:</b></i> </li>
    <li><i><b>Portfolio Reflections:</b></i>
    <br/>LO X.X.X - Students should be able to ...
          </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li><a href="http://computationaltales.blogspot.com/p/posts-by-topic.html" target="_blank">The Computational Fairy Tales blog</a> (which has a printed book as well) has a number of tales written to illustrate searching, sorting and other programming concepts.</li>
    <li><a href="http://en.wikipedia.org/wiki/Binary_search_algorithm" target="_blank">Binary Search Algorithm on Wikipedia</a></li>
    <li><a href="http://en.wikipedia.org/wiki/Linear_search" target="_blank">Linear Search on Wikipedia</a></li>
    <li><a href="http://balance3e.com/Ch8/search.html" target="_blank">Interactive binary search demo</a> -- Give a list of state abbreviations arranged in alphabetical order (e.g., CT, NY), this demo traces the binary search algorithm as you search for different abbreviations in the list.   </li>
    <li><a href="http://www.youtube.com/watch?v=wNVCJj642n4" target="_blank">Binary and Linear Search Algorithms</a> (6:24 video) This videos visually shows how the binary and linear search algorithms are executed. It shows how to search for a particular integer in an array of integers, shows some pseudocode, and talks about the speed and efficiency of each algorithm with comparisons.</li>
    <li><a href="http://www.youtube.com/watch?v=CX2CYIJLwfg" target="_blank">Linear Search</a> (3:32 video) This video provides some real life examples of linear searching along with searching for a number in an array. The video also discusses the pseudocode and how a linear search is performed.</li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <ul>
    <li><a href="http://www.miniplay.gr/?view=game&amp;gid=76" target="_blank">Guess who?</a> (Interactive game) Guessing game against the computer where asking the right Y/N questions, reduces the list of answers. See also this article which gives a <a href="http://blog.teamtreehouse.com/binary-search-or-how-to-win-at-guess-who" target="_blank">Binary Search strategy for winning at Guess Who?</a></li>
    <li><a href="http://video.franklin.edu/Franklin/Math/170/common/mod01/binarySearchAlg.html" target="_blank">Interactive binary search demo with Pascal code</a> -- This demo includes displays the binary search algorithm in Pascal, which isn't all that different from the pseudocode we've used in other algorithm examples.</li>
    </ul>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li><div class="hover eu yui-wk-div" data-id=""></div></li> <!-- for an EU -->
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. poll:: mcsp-5-3-1
    :option_1: Strongly Agree
    :option_2: Agree
    :option_3: Neutral
    :option_4: Disagree
    :option_5: Strongly Disagree
  
    I am confident I can teach this lesson to my students.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-5-3-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>