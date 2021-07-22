.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Pseudo Random Numbers
=====================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['4.07']);
          generateHovers();
      }); 
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=23&amp;lesson=65" target="_blank" title="">This lesson</a> describes how computers <i><b>model</b></i> randomness using relatively simple mathematical functions, such as modular arithmetic (sometimes called clock arithmetic).  It reinforces the enduring understanding that models use abstractions — in this case mathematical constructs — to represent phenomena.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p>Complete the activities for <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=23&amp;lesson=65" target="_blank" title="">Mobile CSP Unit 4 Lesson 4.7: Pseudo Random Numbers</a>. 
    
    </p></div>
    <h3>Materials</h3>
    <ul>
    <li>Computer lab with projection system</li>
    <li><a href="https://docs.google.com/presentation/d/1VWdfhZcI20fjG9koi6hkJnW5eiA85vnoeO6RVJGD9j4" target="blank">
           Pseudo Random Numbers: Slides (not narrated)</a> |
          <a href="https://docs.google.com/a/css.edu/document/d/1uqfp7z-oHA2JOaOU2j0JxFAL8E9nvjF1Q2_V68L9Ofk/edit" target="_blank">Handout</a></li>
    <li>Optional - Paper and pencils for paper-based Chaos activity</li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><i>Adapted from the <a href="https://docs.google.com/document/d/1Cz_eoKVBeeg5foqKk4b51Tjb5p9jD90GJQLVA0xHB-k/edit" target="_blank">Randomness in Stochastic Models</a> lesson plan.</i></li>
    <li><b>Hook/Motivation (10 minutes)</b> Ask students for words or situations where they might expect to see randomness present. Write these words on the board.
    Show them sets of numbers and ask them which they think are random and which are not.
       <ul>
    <li>1, 2, 3, 4, 5</li>
    <li>6, 5, 6, 3, 3</li>
    <li>4, 4, 4, 4, 4</li>
    <li>3, 2, 3, 4, 1</li>
    </ul>
    <b>Explanation:</b> The answer is that we don’t know which of the above sets of numbers are randomly-generated. The fact that some of them seem to resemble a pattern reflects on what we have learned and experiences, not whether they are random. To an alien race, option d might follow a pattern they are aware of. The fact that we don’t see randomness in options a and c is part of a larger philosophical discussion known as the <a href="http://en.wikipedia.org/wiki/Anthropic_principle" target="_blank">Anthropic Principle</a>.
           <br/><i>What makes numbers random are not the results but the method used to determine the numbers.</i>
    <br/><b>Dilbert Joke:</b>  Here's a nice cartoon from Scott Adams' <a href="http://dilbert.com/strip/2001-10-25" target="_blank">Dilbert Cartoon Strip</a> that reinforces the previous point.</li>
    <ul>
    <li>For each scenario, ask the students to describe what they would do to ensure their method was random:
          <ul>
    <li>Picking a card from a deck. A: Example - Close your eyes while choosing.</li>
    <li>Rolling a dice. A: Example - Placing the dice in a cup to shake.</li>
    <li>Driving a car to a destination. A: Example - Flip a coin to determine the direction at each intersection.</li>
    <li>Selecting a word in the dictionary. A: Example - Letting the book fall open to a page.</li>
    </ul>
    </li>
    <li>Can a computer generate random numbers? Why or why not? A: A computer is deterministic, that is, it follows instructions and is incapable of making independent decisions needed for creating a random number. However, some random number generators use information from sensors or human interaction to generate real random numbers. Pseudo-random numbers have faults but are sufficient for most applications.</li>
    </ul>
    <li><b>Experiences and Explorations (30 minutes):</b>
    <ul>
    <li><b>Generate Random Sequences (10 minutes):</b> Have the students <a href="http://faculty.rhodes.edu/wetzel/random/mainbody.html#imagine" target="_blank">complete the first set of activities</a> (up to the table) to generate an imaginary sequence of coin flips.</li>
    <li><span class="yui-non"><b>Optional - Chaos Game (10 minutes):</b> <span style="line-height: 15.86px;">With the students, b</span>efore you say anything, place three large dots on the board so that they represent the corners of an equilateral triangle. Label the dots A , B, and C. Explain to the class that you are going to start at a random place on the board, place a dot, and call on them one by one to have them choose A, B, or C. Then, place a small dot half way between the last dot drawn and the corner called out by the student. Once everyone has had a chance to call out a corner, ask the class if anyone sees a pattern.
            Ask what the class thinks will happen if this process is continued for a really long time. Demonstrate the <a href="http://www.shodor.org/interactivate/activities/TheChaosGame/" target="_blank" title="">computer version of The Chaos Game</a>, which results in a 
            Sierpinski's triangle pattern emerging. <i>Explain that the seemingly random process resulted in a familiar pattern and that is similar to how pseudo number generators work. (</i></span><span style="line-height: 15.86px;">Never seen the Chaos Game? </span><a href="https://www.youtube.com/watch?v=droTYSmSGHg" style="line-height: 15.86px;" target="_blank" title="">Watch this video</a><span style="line-height: 15.86px;"> to see it in action.)</span></li>
    <li><b>Lecture (15 minutes):</b> Either show the videos on Mobile CSP or use the slides to present the material to the students. If you are showing the slides, you can use <a href="https://docs.google.com/a/css.edu/document/d/1uqfp7z-oHA2JOaOU2j0JxFAL8E9nvjF1Q2_V68L9Ofk/edit" target="_blank">this handout</a> to have them complete the exercises during the presentation.</li>
    <li><b>Video (5 minutes):</b> Show the <a href="http://youtu.be/7Wkubf1PrWg" target="_blank">video on slot machines at casinos</a>, which will be needed for their portfolio reflection.</li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (5 minutes):</b> Summarize the main points about randomness and then have students complete their portfolio reflection.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    <ul>
    <li>Topic 3.3 Mathematical Expressions</li>
    <li>Topic 3.9 Developing Algorithms</li>
    </ul>
    </div>
    <h3 class="assessment">Assessment Opportunities</h3>
    <div class="yui-wk-div">
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p><b>Assessment Opportunities</b></p>
    <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.</p>
    <ul>
    <li><i><b>Interactive Exercises:</b></i> </li>
    <li><i><b>Portfolio Reflections:</b></i>
    <br/>LO X.X.X - Students should be able to ...
          </li>
    <li><i><b>In the XXX App, look for:</b></i>
    </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li><a href="http://www.random.org/" target="_blank">Random.org</a> - especially the <a href="http://www.random.org/randomness/" target="_blank">Intro to Randomness post</a></li>
    <li><a href="http://youtu.be/9rIy0xY99a0?list=UU6nSFpj9HTCZ5t-N3Rm3-HA" target="_blank">VSauce - "What is Random?"</a></li>
    </ul>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">
    <p>If you want a deeper dive into the Chaos Game, the lesson can be extended by having the students play the game themselves on paper first, and then use the online simulation to see the patterns. A full <a href="http://www.shodor.org/interactivate/lessons/FractalsAndTheChaos/" target="_blank">lesson plan</a> is included on the Shodor site.</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: Shodor - Fractals and Chaos</h3>
    <div class="yui-wk-div">
    <ul>
    <li><a href="http://www.shodor.org/interactivate/lessons/FractalsAndTheChaos/" target="_blank">Shodor - Fractals and Chaos</a></li><li><a href="https://www.youtube.com/watch?v=droTYSmSGHg" target="_blank" title="">Chaos Game Video</a></li>
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
    <li> How does this lesson help students toward understanding how pseudo randomness is used to model randomness in computer simulations and games? </li>
    <li>Is there anything else you would need to have or know to teach this lesson effectively? What specific elements of this lesson (examples, activities, formative assessments) might you want to change?</li>
    </ul>
    <p>
    
.. poll:: mcsp-4-7-1
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


    
.. fillintheblank:: mcsp-4-7-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    </div>
    </div>