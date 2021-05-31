.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Logo Part 2
===========

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['5.02']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=24&amp;lesson=167" target="_blank" title="">This lesson</a> introduces the concept of parameters as a means of creating procedures that can be more easily reused in a program. Students use an updated version of the Logo app that includes parameters for the forward and turn procedures to change the </p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for 
        Complete the activities for <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=24&amp;lesson=167" target="_blank" title="">Mobile CSP Unit 5: Lesson 5.2 Logo Part 2</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Presentation system (LCD projector/Interactive whiteboard)</li><li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li><li>Access to mobile device with the Companion app installed or access to the emulator installed on the computer or laptop. </li><li>Logo Part 2 Tutorial (video or handout)</li>
    <li>Graphing paper - You can print graph paper from <a href="http://www.printablepaper.net/">www.printablepaper.net</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> Discuss the Logo Part 1 tutorial and its limitations. First ask the students to summarize what the program did. Then ask the students what they think might make the program better.  Hopefully students were frustrated by the weakness of the forward  and move commands in the previous lesson and will be receptive to introducing parameters into the forward(N) and turn(D) procedures.
        <p>Another possible hook is to go through the song <a href="https://en.wikipedia.org/wiki/This_Old_Man#Lyrics" target="_blank">This Old Man</a> and have students point out the repeated lines and then create parameterized procedure calls for each verse like verse("one","thumb"), verse("Two","shoe"), etc. to introduce procedural abstraction with parameters.</p></li>
    <li><b>Experiences and Exploration (30 minutes):</b>
    <ul>
    <li><b>Parameters Introduction (15 minutes):</b> Introduce the concept of parameters for the forward and turn procedures. On the board, develop new algorithms for different sized squares or have the students rewrite their drawFace procedure from the previous lesson using the more powerful set of procedures. Discuss how parameters make the procedures more general (more abstract) and why this is useful. Discuss how the students have begun to evaluate the Logo 1 algorithms for efficiency. As they will see, there are more efficient ways to write algorithms and they should check that the algorithms they will write for the Logo 2 lesson are <i>efficient</i> and <i>clear</i>.</li>
    <li><b>Programming (20 minutes):</b> Have the students open the Logo Part 2 (with parameters) tutorial and have them complete the exercises on their own. You may need to go over angles. The shapes are drawn using exterior angles where 360/number of sides. So for a triangle, it's 360/3 sides = 120 degree turns. See solution file below under Assessments.</li>
    </ul> </li>
    <li><b>Rethink, Reflect, and Revise (10 minutes):</b> Review the lessons learned about algorithms and procedural abstraction.  Have students post a reflection on their portfolio and complete the interactive exercises. One of the main lessons should be that our abstractions — i.e., the particular set of procedures we use — have an enormous impact on our algorithms.  Procedural abstraction makes it easier an algorithm by raising the level of abstraction.  To illustrate this, ask them to think about what the algorithm for a face would if we had to describe it completely in terms of just forward and turn rather than in terms of square, triangle, and circle.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <h4>Suggested Topic Questions:</h4>
    <ul>
    <li>Topic 3.9 Developing Algorithms</li>
    <li>Topic 3.12 Calling Procedures</li>
    <li>Topic 3.13 Developing Procedures</li>
    </ul>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <h4>Solutions:</h4>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li><a href="https://drive.google.com/open?id=1I88Dqdhj1Lvi_3Bxl0TazZtAYDXjOCOdH5JY13tgbDs" target="_blank">Logo 2 Project Solutions</a>
    </li>
    <li><a href="https://drive.google.com/open?id=1xXVoeEKKfyaEA5FqzIkt_Pnnik4RbRp6" target="_blank">Logo 2 .aia file</a>
    </li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <h4>Assessment Opportunities</h4>
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
    <li><a href="https://docs.google.com/document/d/1jUCUXyI4D5IENS__dZ5hRsfl6YfQMdWXqjNktdacS28" target="_blank">Procedures and Parameters Review Sheet</a> submitted by Anthony Truss at Conard High School in CT.</li>
    </ul>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: </h3>
    <div class="yui-wk-div"></div>
    <h3 class="tips">Teaching Tips: Meaningful Parameter Names</h3>
    <div class="yui-wk-div"><p>This lesson is a good time to reinforce the use of meaningful names for variables, including parameters. Students should avoid the use of ambiguous letters (such as x or y) as parameter names and choose something that is easily recognizable and understandable - and indicates the kind of data that it represents. One clue for students is that if they are using good names, their block will read out aloud like sentences in English.</p></div>
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
    
.. mchoice:: mcsp-5-2-1
    :random:
    :practice: T
    :answer_a: Strongly Agree
    :feedback_a: 
    :answer_b: Agree
    :feedback_b: 
    :answer_c: Neutral
    :feedback_c: 
    :answer_d: Disagree
    :feedback_d: 
    :answer_e: Strongly Disagree
    :feedback_e: 
    :correct: a,b,c,d,e

    I am confident I can teach this lesson to my students.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-5-2-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course.
      :x: Thank you. We will review these to improve the course.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>