.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Binary Numbers
==============

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
      $(document).ready(function() {
          generateFrameworkTable(EKmapping['2.09']);
          generateHovers();
      });
    
    </script>
    <!-- This is the overview paragraph.  The link URL should be to the corresponding lesson on the student branch. -->
    <p class="overview">
    <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=63" target="_blank" title="">This lesson </a> 
      reinforces the enduring understanding that binary sequences can be used to represent all digital data through <em>abstraction</em>. Students learn how to convert numbers to and from different number base systems and that numbers may represent different types of data in different contexts. While this unit introduces the binary and other number systems, Unit 3 will take a more in-depth look at the hexadecimal system, including how it is used in computing.
    </p>
    <!-- This is the framework table, where we describe how this lesson fits into the CSP framework.  -->
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson: </b> Complete the activities for 
        <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=1&amp;lesson=63" target="_blank" title="">Mobile CSP Unit 2 Lesson 2.9: Binary Numbers</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li><a href="https://docs.google.com/presentation/d/1LUi8jpatprooXl5QVUhB3JHwAn7v5WOlzGmdrtm9Z0A" target="_blank">Binary Number Slides</a></li>
    <li><a href="https://docs.google.com/document/d/1okQhwTYVLcXN13QioAH71VUhw5e88vxYZ4sVXvSPANY/edit?usp=sharing" target="_blank">Binary Dot Cards</a></li>
    <li><a href="https://docs.google.com/document/d/10aNql-sT9f8-mKXAEBwA6vhpseB6WIzskWYFiRQYXy0/edit?usp=sharing" target="_blank">Binary/Decimal Worksheet</a> (by Mobile CSP Teacher Ingrid Roche). You will need <b>scissors</b> to cut at dotted lines for the binary converter tool at the bottom of the worksheet. Here's a <a href="https://www.youtube.com/watch?v=geK3_3o1lx4&amp;t=9s" target="_blank">video</a> of how to use the converter tool. Because printers may vary, please print out a sample and adjust if necessary before making copies. </li>
    <li><a href="https://drive.google.com/drive/folders/0BzpuhJ4iqvUfWVFoSnFVX2M2MEk?usp=sharing" target="_blank">(Optional) Number Systems Lesson Assets</a> - Shared by Mobile CSP Teacher Christopher Kerr</li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 90 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> Show the joke on the t-shirt image (also at the beginning of the Mobile CSP lesson). 
    <img src="https://sites.google.com/site/mobilecsp/_/rsrc/1372811641332/lesson-plans/lp-binary-numbers/binary-people.jpg?height=200&amp;width=200" style="float:right"/>The "10" on the T-shirt is using a different number base. In the binary number system, there are only 
    2 digits (0 and 1) so 10 has the value of 2. The decimal system is base-10 and has 10 digits (0, 1, 2, 3, ...9). 
    That system is the one we normally use for numbers. So, the t-shirt really means there are only 2 types of people in the 
    world; those who understand binary and those who don't. Another possible hook is to play the  <a href="http://2048game.com/" target="_blank">2048 game</a> and then ask them what is the sequence 2, 4, 8, 16, etc. (the powers of 2) and tell them we will use the powers of 2 to convert binary to decimal (base 10) numbers. </li>
    <li><b>Experiences and Explorations (80 minutes):</b>
    <ul>
    <li>Presentation: Using the <a href="https://docs.google.com/presentation/d/1LUi8jpatprooXl5QVUhB3JHwAn7v5WOlzGmdrtm9Z0A/" target="_blank" title="">slide deck</a> (through slide 6) or by showing the video, go through the introduction of binary numbers.</li>
    <li>Discussion: Binary counting - watch the CS Unplugged video. We recommend that you act it out with your students, using <a href="https://docs.google.com/document/d/1okQhwTYVLcXN13QioAH71VUhw5e88vxYZ4sVXvSPANY/edit?usp=sharing" target="_blank">Binary Dot Cards</a> which you should print out before class. In this activity, only have them count up in binary. Bring back the cards later to do conversions. </li>
    <li><span class="yui-non">Activities: You may choose to have your students complete some or all of the activities in each section. Have students work jointly (either in pairs or small groups) to construct a binary odometer that counts to the decimal value of 20. Using paper and pencil, have the students write down the first 20 values of the binary number system starting with 0. You may choose to have the students do this activity by completing the Binary Column of this <a href="https://docs.google.com/file/d/0B5ZVxaK8f0u9NDBQZjhDTlFXY1k" target="_blank" title="">Base Conversion Worksheet</a>.</span></li>
    <ul><li>Explanation: Compare a decimal odometer (10 digits) with a binary odometer (2 digits). Students know how the decimal odometer works: It starts at 000. The rightmost column cycles through the digits 0 through 9 before the next digit to the left is incremented giving 010 (10 miles). For the binary odometer, the rightmost digit cycles from 0 though 1 before the next digit to the left is increment giving 10 (2 miles). The key point here is that in any number system, the wheel in the next column to the left doesn't turn until the wheel in the adjacent column (to the right) turns over to 0. In decimal, the 10s column doesn't turn from 0 to 1 until the 1s column turns from 9 to 0.</li></ul>
    <li>Presentation: Using the <a href="https://docs.google.com/presentation/d/1LUi8jpatprooXl5QVUhB3JHwAn7v5WOlzGmdrtm9Z0A/" target="_blank" title="">slide deck</a> (slide 7-20) or by showing the video, go through converting Binary to Decimal and Decimal to Binary.</li><ul><li>Also, point out that both binary and decimal odometers are positional number systems. Point out that numbers, including binary data, are represented by bits and are used to store digital data.
    </li></ul>
    <li>Activities: You may have your students complete some or all of the activities listed in each section, but you should make sure that your students can convert numbers between binary (base 2) and decimal (base 10). We recommend that you use <a href="https://docs.google.com/document/d/1jU_TLqo71jLKdEXDSqmNlbiVlFOAnqIimR3LR-JO2IA/edit?usp=sharing" target="_blank">Binary Converter Tool</a> (print double-sided and cut at dotted lines to make tabs of the 1's so they can be flipped backwards to cover the 0's) or the  <a href="https://appinventor.trincoll.edu/csp/odometer/binaryConverter.html" target="_blank">online binary converter tool</a> and the <a href="https://docs.google.com/document/d/10aNql-sT9f8-mKXAEBwA6vhpseB6WIzskWYFiRQYXy0/edit?usp=sharing" target="_blank">Binary/Decimal Worksheet.</a>  If your class has time, have them explore the <a href="https://maya.nmai.si.edu/maya-sun/maya-math-game?game=practice-1" target="_blank">Maya Math Game (a base 20 number system)</a> in pairs.</li>
    </ul>
    </li>
    <li><b>Rethink, Reflect and/or Revise (5 minutes):</b> The position number system pattern, base conversion worksheet, and interactive exercises. Discuss: Why do computers use binary?</li>
    </ul>
    <div class="ui-accordion ui-widget ui-helper-reset yui-wk-div" id="accordion" role="tablist">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p><ul><li><span style="font-weight: normal;">Topic 2.1 Binary Numbers</span></li></ul></h4>
    </div>
    <h3 aria-controls="ui-id-2" aria-expanded="false" aria-selected="false" class="assessment ui-accordion-header ui-state-default ui-corner-all" id="ui-id-1" role="tab" tabindex="0">Assessment Opportunities and Solutions</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-1" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-2" role="tabpanel" style="display: none;">
    <p><b>Solutions:</b></p>
    <ul>
    <li>Note: Solutions are only available to verified educators who have joined the <a href="./unit?unit=1&amp;lesson=39" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</li>
    <li>
    <a href="https://docs.google.com/document/d/1ZhQjFHkKRaQZIe_KeI9vRj3NewScZbwXByaG-kLlilA/edit?usp=sharing" target="_blank">Binary/hex conversion worksheet answers</a>.</li>
    <li>
    <a href="https://docs.google.com/file/d/0B6fFiZdZdzwSajVaUGRhMldOS2c" target="_blank">Completed base conversion worksheet</a>.</li>
    <li><a href="https://drive.google.com/open?id=1Us4_AJcI_9Xja_1lTTr6RJmI3Ko57W4Kisv7hmXv5cw" target="_blank">Quizly Solutions</a>
    </li>
    <li><a href="https://sites.google.com/a/css.edu/jrosato-cis-1001/" target="_blank">Portfolio Reflection Questions Solutions</a>
    </li>
    </ul>
    <p><b>Assessment Opportunities</b></p>
    <ul>
    <li>Formative Assessment: <a href="https://docs.google.com/file/d/0B5ZVxaK8f0u9NDBQZjhDTlFXY1k/edit" target="_blank">Base conversion worksheet</a>
           <a href="https://docs.google.com/file/d/0B6fFiZdZdzwSajVaUGRhMldOS2c" target="_blank">Completed base conversion worksheet</a>
    </li>
    <li>Formative Assessment: Interactive exercises in Mobile CSP lesson</li>
    </ul>
    </div>
    <h3 aria-controls="ui-id-4" aria-expanded="false" aria-selected="false" class="diff-practice ui-accordion-header ui-state-default ui-corner-all" id="ui-id-3" role="tab" tabindex="-1">Differentiation: More Practice</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-3" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-4" role="tabpanel" style="display: none;">
    <ul>
    <li>The <a href="http://csunplugged.org/binary-numbers" target="_blank">CS Unplugged Binary Counting activity</a> may also be used as a lesson starter or an activity for this lesson.</li>
    <li>Here's a <a href="http://inventwithpython.com/blog/2013/06/20/decimal-binary-and-hexadecimal-odometers/" target="_blank">cool interactive demonstration</a> that compares decimal, binary, and hexadecimal odometers. You can let the students try these out after they've worked on trying to figure out the binary odometer.</li>
    </ul>
    </div>
    <h3 aria-controls="ui-id-6" aria-expanded="false" aria-selected="false" class="diff-enrich ui-accordion-header ui-state-default ui-corner-all" id="ui-id-5" role="tab" tabindex="-1">Differentiation: Enrichment</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-5" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-6" role="tabpanel" style="display: none;">
    <ul>
    <li>Learn about Octal (base 8) and Hexadecimal (base 16) number systems which are also used in computer science: <a href="https://www.youtube.com/watch?v=qfgSLHxlJQs" target="_blank">video</a>
    (<a href="http://www.teachertube.com/video/hexoctal-348088" target="_blank">Teacher Tube version</a>), <a href="https://docs.google.com/presentation/d/1JIfA9xltl36VtOq641Dw2-TcKXQ30sBTyH6BW2YP-WQ/" target="_blank" title="">slide deck</a>, <a href="https://mobile-csp.org/webapps/numbers/hexodometer.html" target="_blank">hexodometer</a>, <a href="https://docs.google.com/document/d/1a0BwOKTgmv00ywzwfjwgVNDQvsy2pdsyDcWNSvzODiI/edit" target="_blank">binary/hex worksheet</a> </li>
    <li>The <a href="http://www.wordfreegames.com/game/binary-game.html" target="_blank">Binary Game</a> turns learning binary numbers into a Tetris-like game.  It's fun!</li>
    <li>The <a href="https://maya.nmai.si.edu/maya-sun/maya-math-game" target="_blank">Mayan Math Game </a> lets students explore the ancient base-5 and base-20 arithmetic system developed by Mayans. This article <a href="http://bilingualeducationcurriculum.weebly.com/uploads/2/2/3/4/22342120/chicanos_have_math.pdf">article</a> explains that Chicano cultural achievements such as this are often ignored in U.S. education and could be a powerful motivator.</li>
    <li>Here's a <a href="http://inventwithpython.com/blog/2013/06/20/decimal-binary-and-hexadecimal-odometers/" target="_blank">cool interactive demonstration</a> that compares decimal, binary, and hexadecimal odometers. You can let the students try these out after they've worked on trying to figure out the binary odometer.</li>
    </ul>
    </div>
    <h3 aria-controls="ui-id-8" aria-expanded="false" aria-selected="false" class="bk-knowledge ui-accordion-header ui-state-default ui-corner-all" id="ui-id-7" role="tab" tabindex="-1">Background Knowledge: Number Bases and Odometers</h3>
    <div aria-hidden="true" aria-labelledby="ui-id-7" class="ui-accordion-content ui-helper-reset ui-widget-content ui-corner-bottom yui-wk-div" id="ui-id-8" role="tabpanel" style="display: none;">
    <p>Different number bases can be used for counting. In decimal, 
          1 digit can represent 10 (10<sup>1</sup>) different values, 2 digits can represent 100 (10<sup>2</sup>) 
          different values,  3 digits can represent 1000 (10<sup>3</sup>) different values. But in binary, 1 digit 
          can represent 2 (2<sup>1</sup>) different values, 2 digits can represent 4 (2<sup>2</sup>) different values,  
          3 digits can represent 8 (2<sup>3</sup>) different values.
    
          <br/>
    <br/>
    <b>Math Facts:</b>
    </p><ul>
    <li>Any number to the 0 power is 1 -- e.g., 10<sup>0</sup> = 1</li>
    <li>Any number to the 1 power is the number itself -- e.g., 10<sup>1</sup> = 10</li>
    <li>Any number to the 2 power is the number squared -- e.g., 10<sup>2</sup> = 10 * 10 = 100</li>
    <li>Any number to the 3 power is the number cubed -- e.g., 10<sup>3</sup> = 10 * 10 * 10 = 1000</li>
    <li>And so on. </li>
    </ul>
    <br/>
    <b>Computer facts:</b>
    <ul>
    <li>The smallest piece of information in a computer is a <i><b>bit</b></i> which stands for binary digit.</li>
    <li>That is, in a single memory location the computer can store a 1 or a 0.</li>
    <li>Why do computers use the binary system instead of the decimal system?</li>
    <li>Because in electronics it is easier to distinguish between two voltage levels (high, low) or (on, off) 
            or (1, 0), than to distinguish among 10 voltage levels.</li>
    </ul>
    <br/>
    <b>Binary Counting:</b>
    <br/> One way to help students count in binary is to explain the number places. For example, 
        if you want to represent 32 in binary, it is 100000, where the 1 is in the 32s place. 
        The places are as follows:
        <br/>
    <table>
    <tbody>
    <tr>
    <td>32s</td><td>16s</td><td>8s</td><td>4s</td><td>2s</td><td>1s</td>
    </tr>
    <tr>
    <td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td>
    </tr>
    </tbody>
    </table>
    <br/>
    <b>Odometers.</b>
    <br/>Compare a decimal odometer (10 digits) with a binary odometer (2 digits). 
        Students know how the decimal odometer works: It starts at 000.  The rightmost column cycles 
        through the digits 0 through 9 before the next digit to the left is incremented giving 010 (10 miles). 
         For the binary odometer, the rightmost digit cycles through 0 though 1 before the next digit to 
        the left is increment giving 10 (2 miles).   <b> The key point here is that in any number system, 
        the wheel in the next column to the left doesn't turn until the wheel in the adjacent column 
        (to the right) turns over to 0. </b>  In decimal, the 10s column doesn't turn from 0 to 1 until 
        the 1s column turns from 9 to 0.  Also, point out that both binary and decimal odometers are 
        <i style="font-weight: bold;">positional number systems. </i>Point out that numbers, including 
        binary data, are represented by bits and are used to store digital data. What other number bases are 
        there and what type of data are they used for? Hexadecimal is often used for colors in images.
        <br/>
    <br/>
    <b>Positional Number Systems. </b> This explanation may be too abstract for some students, but if 
        they can see this pattern it's a real win. 
        <br/>
        549 in <font color="#ff0000">base<b>10</b></font> 
        = (5 * 100) + (4 * 10) + (9 * 1) 
        = (5 * <b><font color="#ff0000">10<sup>2</sup></font></b>) + 
          (4 * <b><font color="#ff0000">10<sup>1</sup></font></b>) +  
          (9 * <b><font color="#ff0000">10<sup>0</sup></font></b>) 
        = 549
        <br/>
    <br/>
        101 in <font color="#ff0000">base</font> <b><font color="#ff0000">2</font></b> 
        = (1 * 4) + (0 * 2) + (1 * 1)   
        = (1 * <font color="#ff0000"><b>2<sup>2</sup></b></font>) + 
          (0 * <font color="#ff0000"><b>2<sup>1</sup></b></font>) + 
          (1 * <b><font color="#ff0000">2<sup>0</sup></font></b>) 
        = 5
    
        <br/>
    <br/>So the pattern in the  <b style="font-style: italic;">positional number 
        pattern</b> is that each digit in the number, going from right to left, is multiplied 
        by the base raised to the power of that digit. 
    
        In symbols:<br/><br/><span style="font-style: italic;">    </span> If we let 
        d<sub>2</sub> and d<sub>1</sub> 
        and d<sub>0</sub> be three digits going from left to right, 
        then a 3-digit number in base <font color="#ff0000" style="font-style: italic; font-weight: bold;">b </font>
    <font color="#000000">would be expressed</font>
    <font color="#000000" style="font-size: 10pt; font-style: italic; line-height: 1.6;">
    <span style="font-style: normal;"> as</span><b> </b></font>
    <font color="#000000" style="font-size: 10pt; line-height: 1.6;"> <br/></font>
    <span style="line-height: 1.6; text-align: center;"><span style="font-size: 10pt;">
                                                  </span>
    <font size="5">d<span style="color: rgb(255, 0, 0); line-height: 17px;"><sub>2</sub> </span>
    <span style="line-height: 17px;"><font color="#000000">* </font><b>
    <font color="#ff0000">b</font><sup style="color: rgb(255, 0, 0);">2</sup>
    <font color="#000000"> + </font></b></span></font></span>
    <font size="5" style="font-style: italic;"><span style="text-align: center; font-style: normal; line-height: 1.6;">d<sub>
    <font color="#ff0000">1</font></sub></span><span style="text-align: center; font-style: normal; color: rgb(255, 0, 0); line-height: 17px;"> </span>
    <span style="text-align: center; font-style: normal; line-height: 17px;"><font color="#000000">* </font>
    <b><font color="#ff0000">b</font><sup style="color: rgb(255, 0, 0);">1</sup>
    <font color="#000000"> + </font></b></span><span style="text-align: center; font-style: normal; line-height: 1.6;">d</span>
    <span style="text-align: center; font-style: normal; color: rgb(255, 0, 0); line-height: 17px;"><sub>0</sub> </span>
    <span style="text-align: center; font-style: normal; line-height: 17px;">
    <font color="#000000">* </font><b><font color="#ff0000">b</font><sup style="color: rgb(255, 0, 0);">0</sup>
    <font color="#000000"> </font></b></span></font>
    </div>
    </div>
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li> How does this lesson help students toward the enduring understanding that a variety of abstractions built on binary sequences can be used to represent all digital data?</li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    <p>
    
.. poll:: mcsp-2-9-1
    :option_1: Strongly Agree
    :option_2: Agree
    :option_3: Neutral
    :option_4: Agree
    :option_5: Disagree
  
    I am confident I can teach this lesson to my students.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    
.. fillintheblank:: mcsp-2-9-2

    What questions do you still have about the lesson or content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course content.
      :x: Thank you. We will review these to improve the course content.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>


    </p>
    </div>
    </div>