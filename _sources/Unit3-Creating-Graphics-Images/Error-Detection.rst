.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Error Detection
===============

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['3.06']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Error-Detection.html" target="_blank" title="">This lesson</a>, which is adapted from <a href="http://csunplugged.org/error-detection/" target="_blank">Computer Science Unplugged</a>, uses a card trick to illustrate how extra bits in a binary sequence can be used to detect certain kinds of errors.  It reinforces the enduring understanding that a variety of abstractions built upon binary sequences can be used to represent all digital data. </p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <!--   End of Framework table. -->
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p><b>The Student Lesson: </b> Complete the activities for 
        <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Error-Detection.html" target="_blank" title="">Mobile CSP Unit 3 Lesson 3.6: Error Detection</a>.
      </p>
    </div>
    <h3>Materials</h3>
    <ul>
    <li>Playing cards or 0/1 cards are useful for this lesson. Here are some options:
         </li><ul>
    <li>
         Set of cards to use on the board (magnetic, large post-it notes or similar that are sticky on both sides)</li>
    <li>Set of cards for groups of 3 students (card stock that has a different color on each side)</li>
    <li>Alternatives (in-person): pennies (heads/tails would be 0/1),  <a href="https://docs.google.com/spreadsheets/d/1xr0EYguJOp6w3f0kSv-kAx1HYJJ0vsEitimI0_L2Q5Q/edit?usp=sharing" target="_blank">0/1 bit cards</a>, deck of playing cards
           </li>
    <li>Alternatives (online teaching): <a href="https://docs.google.com/presentation/d/1Otca6f8zwhLcmOWNXswq7u-nU00hvObzL9cxYJ1qfVo/edit?usp=sharing" target="_blank">Slide where students can move cards into place</a>, <a href="https://deck-of-cards.js.org/" target="_blank">Virtual playing cards</a>, the android widget built into lesson. </li>
    </ul><li><a href="https://docs.google.com/document/d/1G7IQDERipCeZPFf4NheSPOMYmWM0f7wAFgPVnNzPvnE/edit" target="_blank" title="">POGIL handout</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 45 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (5 minutes):</b> Ask the students: Now that you know that all data in a computer are stored in bits, in sequences of binary 0s and 1s, what might an error look like when you store or transmit some data? When data is corrupted it is said to contain an error. <br/>"When data is stored on a disk or transmitted from one computer to another, we usually assume that it doesn’t get changed in the process. But, sometimes things go wrong and the data is changed accidentally. This activity uses a magic trick to show how to detect when data has been corrupted, and to correct it." -CS Unplugged</li>
    <li><b>Experiences and Explorations (30 minutes):</b>
    <ul>
    <li><b>Card Trick Demo (5 minutes):</b> Do the error detection card trick with students using a deck of cards or the online widget or <a href="https://deck-of-cards.js.org/" target="_blank">virtual playing cards</a>. The CS Unplugged <a href="http://www.google.com/url?q=http%3A%2F%2Fcsunplugged.org%2Ferror-detection&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNHfeIDaUAHx78eU5LZUAz0ctD0Xsg" target="_blank">error detection card trick page</a> contains videos of the trick being done. The CS Unplugged <a href="http://csunplugged.org/wp-content/uploads/2014/12/unplugged-04-error_detection.pdf" target="_blank">error detection card trick pdf</a> explains how the trick is done:
             <ul>
    <li>Have a pile of cards ready. The cards could all be black on one side and white on the other, or you could use a deck of playing cards with the face as the white side and the back as the black side, or some printed <a href="https://docs.google.com/spreadsheets/d/1xr0EYguJOp6w3f0kSv-kAx1HYJJ0vsEitimI0_L2Q5Q/edit?usp=sharing" target="_blank">0/1 bit cards</a></li>
    <li>Ask for a student volunteer to layout a 5 x 5 grid of cards. The cards can be in any order.</li>
    <li>When the student has finished laying out the grid, then casually lay out the additional row and column (the parity bits). When adding a card to each row and column, make sure the number of black cards in that row or column is always even. For example, if the row the student volunteer has made has 1 black cards and 4 white cards, then you add a black card to that row to make the total number of blacks in that row 2, an even number. Simply tell the students you are adding these cards to make the trick 'harder." Do not explain how/why you are really adding the extra cards.</li>
    <li>Ask for another student volunteer to switch out any card and replace it with the opposite color card while you leave the room or look away. </li>
    <li>Come back and do the trick - "magically" spot which card was flipped while you were looking by finding which row and column has an odd number of black cards.</li>
    <li>Ask the students if they have any insight on what you may have done.</li>
    </ul>
    </li>
    <li><b>POGIL Activity (25 minutes):</b> Break students into teams of 3-4 and have them complete the critical thinking questions. Make sure students are following their roles and that each student in the group understands the card trick.</li>
    </ul>
    </li><li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Ask the students to write a reflection in their Google portfolio that describes the error detection card trick, how it is performed, and what they learned about error detection. If time permits, have the students try some interactive exercises.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p> <span style="font-weight: normal;">None</span></h4>
    </div>
    <h3 class="assessment">Assessment Opportunities and Solutions</h3>
    <div class="yui-wk-div">
    <p><b>Solutions</b> 
    <i>Note: Solutions are only available to verified educators who have joined the <a href="../Unit1-Getting-Started/PD-Joining-the-Forum.html" target="_blank">Teaching Mobile CSP Google group/forum in Unit 1</a>.</i></p>
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
    <li><i><b>In the XXX App, look for:</b></i>
    </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">If students are having trouble understanding the card trick, have them watch the <a href="https://youtu.be/gBPZOpT4DPU?t=1m42s" target="_blank">CS Unplugged video</a> that shows the solution.</div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div">Have students explore the conditions under which two cards being flipped <i>does</i> work and when it <i>does not</i> work.</div>
    <h3 class="bk-knowledge">Background Knowledge: Error Detection Card Trick</h3>
    <div class="yui-wk-div">
    <p><a href="http://www.mathmaniacs.org/lessons/A-errordet/" target="_blank">MATHmaniaCS</a> provides a very detailed explanation on how you can do the magic trick with your students.</p>
    <h4>Answers to Above Questions</h4>
    <p>For the 5 × 5 table,  if you count the number of 1s you get the following
    results:
    </p><blockquote>
    <pre>Row   #of 1s         Column     #1s
    1       1                 1      2
    2       2                 2      2
    3       1                 3      1
    4       1                 4      0
    5       1                 5      1
    </pre>
    </blockquote>
    <p>For the 6 × 6 table, if you count the number of 1s you get the following results:
    </p><blockquote>
    <pre>Row   #of 1s         Column     #1s
    1       2                 1      2
    2       2                 2      2
    3       2                 3      2
    4       2                 4      0
    5       2                 5      2
    6       2                 6      4
    </pre>
    </blockquote>
    <p>The difference in the 6 × 6 case is that all of the
    rows and columns have an <i><b>even number of 1s</b></i>.
    If you "flip" a 1 to a 0 or a 0 to a 1 in the 6 × 6 table, 
    you will destroy this pattern, making 1 row and 1 column have
    an odd number of 1s.  The intersection of that row and column
    will indicate the bit that was flipped. For example, count the 0s
    and 1s in rows and columns of this 6 × 6 table and you'll
    see that the rows and columns with an odd number of bits intersect
    at the flipped (<font color="red">red</font>) bit. 
    
    </p><p>The 6 by 6 table with a flipped bit. The <font color="blue">blue numbers</font> give
    the number of 1s in each row and column.
    </p><blockquote>
    <table border="0">
    <tbody><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td><font color="blue">2<font></font></font></td></tr>
    <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td><font color="blue">2<font></font></font></td></tr>
    <tr><td>0</td><td>0</td><td><font color="red">0</font></td><td>0</td><td>0</td><td>1</td><td><font color="red">1<font></font></font></td></tr>
    <tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td><font color="blue">2<font></font></font></td></tr>
    <tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td><font color="blue">2<font></font></font></td></tr>
    <tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td><font color="blue">2<font></font></font></td></tr>
    <tr><td><font color="blue">2<font></font></font></td><td><font color="blue">2<font></font></font></td><td><font color="red">1<font></font></font></td><td><font color="blue">0<font></font></font></td><td><font color="blue">2<font></font></font></td><td><font color="blue">4<font></font></font></td><td><font color="blue"> <font></font></font></td></tr>
    </tbody></table>
    </blockquote>
    </div>
    <h3 class="tips">Teaching Tips: Practice, Practice, Practice</h3>
    <div class="yui-wk-div"><p>Practice the card trick with friends or family so that you feel comfortable performing it in front of the students. If not, show the demo video instead until you have it down. You can order your own <a href="htt://www.notabletechnicalwomen.org/" target="_blank">Notable Women in Computing</a> deck of cards—the same ones used in the video demo.</p></div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How does this lesson help students toward the enduring understanding that the way a computer represents data internally is different from the way the data is interpreted and displayed for the user? <div class="hover eu yui-wk-div" data-id="DAT-1">[EU DAT-1]</div>
    </li>
    </ul>
    <p>
    
.. poll:: mcsp-3-6-1
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


    
.. fillintheblank:: mcsp-3-6-2

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