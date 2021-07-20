.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Abstraction Inside the CPU optional
===================================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['4.09']);
          generateHovers();
      }); 
    
    </script>
    <p class="overview"><a href="https://course.mobilecsp.org/mobilecsp/unit?unit=23&amp;lesson=154" target="_blank" title="">This lesson</a> leads students from a low level programming language to a higher level language in order to illustrate the layers of abstraction at work in a computer. It also illustrates some of the basic concepts around how hardware components work in the computer. There are a number of technical terms that should be reviewed as needed with students.</p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson:</b> Complete the activities for 
        <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=23&amp;lesson=154" target="_blank" title="">Mobile CSP Unit 4 Lesson 4.10: Abstraction: Inside the CPU</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Presentation system (LCD projector/Interactive whiteboard)</li>
    <li>Access to computer, laptop, or Chromebook (install the Companion app on Chromebooks)</li>
    <li>Videos and Simulators Pages:
          <ul>
    <li><a href="https://vimeo.com/107667129" target="_blank" title="">ENIAC Programmers Story Trailer</a></li><li><span class="yui-non"><a></a><a href="https://youtu.be/-70EG8Me1vU" target="_blank" title="">Generation 0 - 4-Bit simulator</a> | <a href="https://mobile-csp.org/webapps/computer/gen0.html" target="_blank" title="">Simulator Page</a></span></li>
    <li><span class="yui-non"><span class="yui-non"><span class="yui-non"><a href="https://youtu.be/_7-44rIkc24" target="_blank" title="">Generation 1</a> | <a href="https://mobile-csp.org/webapps/computer/gen1.html" target="_blank" title="">Simulator Page</a></span></span></span></li><li><span class="yui-non"><span class="yui-non"><a href="https://youtu.be/L5TamiB3Bf0" target="_blank" title="">Generation 2</a> | <a href="https://mobile-csp.org/webapps/computer/gen2.html" target="_blank" title="">Simulator Page</a></span></span></li>
    </ul>
    </li>
    </ul>
    <p></p>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> Show the trailer to the <a href="https://vimeo.com/107667129" target="_blank">ENIAC Programmers Story</a>.  Engage students in a discussion of the skills programmers needed at the time of the ENIAC versus the skills they are learning in this class. Responses might include that they need more math skills to program on the ENIAC, but they should also be able to identify that they needed to think abstractly and solve problems, including debugging errors, as well as work collaboratively in teams.</li>
    <li><b>Experiences and Exploration (30 minutes):</b> The lesson consists of three short videos, interspersed with self-check questions and activities.  Students should     watch the videos, and then <b>work together either in pairs, or teams</b> to work out the solutions to the questions and problems.
        <br/>All of the problems focus on a <b>4-bit Computer Simulator</b> that models the development of a digital computer through several generations, starting with the raw machine, which has to be programmed directly in machine language (<a href="https://www.mobile-csp.org/webapps/computer/gen0.html" target="_blank" title="">Generation 1</a>), through the use of primitive software tools (<a href="https://www.mobile-csp.org/webapps/computer/gen1.html" target="_blank" title="">Generation 2</a>), through the use of an Assembly Language (<a href="https://www.mobile-csp.org/webapps/computer/gen2.html" target="_blank" title="">Generation 3</a>).
        <br/>The theme of the lesson is <i><b>abstraction</b></i>.  Try to get students to appreciate the role 
          that ever more sophisticated software abstractions have played in making computers more accessible.
          Try to draw a comparison between the <b>primitive nature  of machine language and assembly language</b>,
          which the ENIAC women used, and the sophisticated nature of the App Inventor language that they are using.
    
        <br/>Another important fact to point out is that the 4-bit Simulator, as simple and primitive as it is, 
          accurately models today's powerful computers, including their smart phones.  At the heart of 
          today's computers are still components such as <b>RAM</b> and the <b>CPU</b>; today's computer's are
          still based on a <b>fetch-execute cycle</b>, in which <b>machine language instructions</b> are interpreted
          and executed by the CPU.  And today's programs, regardless of what <b>high-level language</b> they are
          written in, still need to be translated (by <b>software</b>) into machine language before they can be run 
          on a computer.  
      </li>
    <li><b>Rethink, Reflect, and Revise (10 minutes):</b> One of the themes of this lesson is the usefulness of <i><b>models</b></i> and <i><b>simulations</b></i> in helping us understand complex phenomena.  Engage students in a discussion of the 4-bit Computer Simulator and how it helped deepen their understanding of how computers work.</li>
    </ul>
    <div class="ui-accordion ui-widget ui-helper-reset yui-wk-div" id="accordion" role="tablist">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p>
    </div>
    <h3 aria-controls="ui-id-2" aria-expanded="false" aria-selected="false" class="assessment ui-accordion-header ui-state-default ui-corner-all" id="ui-id-1" role="tab" tabindex="0">Assessment Opportunities</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-1" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-2" role="tabpanel" style="display: none;">
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
    <h3 aria-controls="ui-id-4" aria-expanded="false" aria-selected="false" class="diff-practice ui-accordion-header ui-state-default ui-corner-all" id="ui-id-3" role="tab" tabindex="-1">Differentiation: More Practice</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-3" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-4" role="tabpanel" style="display: none;">
    <p>If students are struggling with lesson concepts, have them review the following resources:</p>
    <ul>
    <li><a href="http://www.hartismere.com/CPU-Fetch-Decode-Execute-Animation-20398" target="_blank">A nice animation</a> of a slightly more detailed fetch/execute cycle.
        </li>
    </ul>
    </div>
    <h3 aria-controls="ui-id-6" aria-expanded="false" aria-selected="false" class="diff-enrich ui-accordion-header ui-state-default ui-corner-all" id="ui-id-5" role="tab" tabindex="-1">Differentiation: Enrichment</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-5" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-6" role="tabpanel" style="display: none;"><p>The <a href="http://eniacprogrammers.org/see-the-film/" target="_blank">story of the ENIAC programmers</a> is now told in a feature-length documentary that is freely avaiable for individual viewing. It might be a nice movie to watch in class (20 minutes, $5 to stream).</p>
    </div>
    <h3 aria-controls="ui-id-8" aria-expanded="false" aria-selected="false" class="bk-knowledge ui-accordion-header ui-state-default ui-corner-all" id="ui-id-7" role="tab" tabindex="-1">Background Knowledge: Fetch-Execute Cycle</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-7" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-8" role="tabpanel" style="display: none;">
    <p>The 4-bit Simulator models the computer's <a href="https://en.wikipedia.org/wiki/Instruction_cycle" target="_blank">fetch-execute cycle</a>, which is summarized in the 4-steps in this image: </p>
    <img align="left" src="../_static/assets/img/1200px-The_Fetch-Execute_Cycle.svg.png" width="400px"/>
    <p>In step 1, the CPU fetches a machine language instruction from main memory (RAM). In step 2 it decodes the instruction.  This is done automatically by the hardware of the computer. For example, for an instruction with a 4-bit opcode, such as 0011, this would send signals over certain wires in the CPU (corresponding to the 1s in the opcode) that would cause certain actions to happen. If its an add instruction, these wires would connect to the CPU's Arithmetic Logic Unit (ALU).   In step 3, the CPU fetches whatever data is needed to carry out the instruction.  If it's an add instruction, then the numbers to be added are fetched into the CPU's internal data registers. And finall, in step 4, the CPU carries out the instruction — by actually performing the addition, as an example. 
        </p>
    </div>
    <h3 aria-controls="ui-id-10" aria-expanded="false" aria-selected="false" class="bk-knowledge ui-accordion-header ui-state-default ui-corner-all" id="ui-id-9" role="tab" tabindex="-1">Background Knowledge: Female Role Models</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-9" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-10" role="tabpanel" style="display: none;">
    <p>It's important to include role models for underrepresented groups in CS, including women and minorities. People can name many computer scientists, but few of them are men. By providing role models that students can identify with, and feel like they could see themselves in the field, they are more likely to consider that field as a potential career.</p>
    <p>So few women study computer science today, relative to men, while women played a leadership role in CS when the discipline was just starting. The percentage of females who earn a BS degree in CS, which peaked in 1986 at 37%, has since declined to around 17%. Another good source for data on women in computing is the <a href="https://www.ncwit.org/infographic/3435" target="_blank">National Center for Women in IT (NCWIT)</a>.</p>
    <img align="center" src="../_static/assets/img/women2-bachelordegress.jpg" width="500"/>
    </div>
    <h3 aria-controls="ui-id-12" aria-expanded="false" aria-selected="false" class="tips ui-accordion-header ui-state-default ui-corner-all" id="ui-id-11" role="tab" tabindex="-1">Teaching Tips: Technical Terms</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-11" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-12" role="tabpanel" style="display: none;">
    <p>It might be useful to have students review some of the technical terms used in this lesson.  This <a href="https://docs.google.com/presentation/d/1uBkj-Mf--0-zwz_Y7Kk1wSYEELWIEQYUGfygSM7J94s" target="_blank">slide presentation</a> summarizes the key terms and concepts and includes a matching activity at the end. </p>
    </div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How do the lesson activities reinforce the computational practice of <div class="hover ctp yui-wk-div" data-id="3">abstracting</div> for students?</li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    
.. mchoice:: mcsp-4-9-1
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


    
.. fillintheblank:: mcsp-4-9-2

    What questions do you still have about the lesson or the content presented? |blank|

    - :/.*/i: Thank you!
      :x: 


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </div>
    </div>