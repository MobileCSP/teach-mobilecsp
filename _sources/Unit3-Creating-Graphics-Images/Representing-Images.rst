.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Representing Images
===================

.. raw:: html

        <div class="MCSP-lesson-content">
    <script>
     $(document).ready(function() {
          generateFrameworkTable(EKmapping['3.03']);
          generateHovers();
      });
    
    </script>
    <p class="overview"><a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Representing-Images.html" target="_blank" title="">This lesson</a> reinforces two important enduring understandings. 
    First, a variety of abstractions built upon binary sequences can be used 
    to represent all digital data.
    In this lesson, students see how digital sequences can be used to represent images.   
    And, second, there are always trade-offs when representing information as digital data.   
    In this lesson, we explore trade-offs that occur when compressing images: 
    lossy compression algorithms trade the loss of some bits from the image in order to get 
    higher levels of compression.</p><p class="overview"><span class="hover eu yui-wk-div" data-id="2.1"><br/></span></p>
    <table border="" class="framework" id="genTable" width="100%"></table>
    <div class="pd yui-wk-div">
    <h3>Professional Development</h3>
    <p>Complete the activities for <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit3-Creating-Graphics-Images/Representing-Images.html" target="_blank" title="">Unit 3 Lesson 3.3: Representing Images</a>. 
    </p></div>
    <h3>Materials</h3>
    <ul>
    <li>Projection system</li>
    <li>Printed copies of the <a href="https://docs.google.com/document/d/1AkIwOQLTU4_TonpRh3LEqoLMXWiVdZ4AiYf1y-qWIEI/edit?usp=sharing" target="_blank" title="">Image Representation Activity worksheet</a> (adapted  from <a href="http://csunplugged.org/wp-content/uploads/2014/12/unplugged-02-image_representation.pdf" target="_blank">CS Unplugged</a>)   </li><li><a href="https://docs.google.com/document/d/1Q4NinpY_-BLSjh9RVO1bD4apZYs4W93WbpX_nbas1Ec/" target="_blank" title="">Image Compression Text Version</a></li><li><a href="https://docs.google.com/presentation/d/1MmKmh7fJKCCfwGzA238VPXZYLkCZvIIUQZ9L-RIDEYQ" target="_blank" title="">Slides</a></li>
    </ul>
    

Learning Activities
--------------------

.. raw:: html

    <p>
    <h3 id="est-length">Estimated Length: 90 minutes</h3>
    <ul>
    <li><b>Hook/Motivation (10 minutes):</b>  Ask students to think about how images are represented on computers. Look at a zoomed in image to see the pixels (<a href="http://introcomputing.org/image-1-introduction.html" target="_blank">example at http://introcomputing.org/image-1-introduction.html</a>). If no one mentions it, explain computers break down images
      into pixels, and that the term pixel is short for "picture element." Discuss image representation with the class, being sure to cover the following points:
        <ul>
    <li>After breaking an image into pixels, computers use a variety of methods to represent each pixel or groups of pixels as numbers.</li>
    <li>Numbers are translated to bits, which are stored and sent like any other data. </li>
    <li>Other computers use the bits to reconstruct image. </li>
    <li>Storing specific information about every single bit would be an enormous amount of data for an image. What are some ways a computer might store an image using less data? Compression techniques!</li>
    </ul>
    </li>
    <li><b>Experiences and Exploration (70 minutes):</b>
    <ul><li>Have students watch the <a href="https://www.youtube.com/watch?v=uaV2RuAJTjQ" target="_blank">CS
          Unplugged video</a> on image compression for a quick look at one way that images are represented and compressed. </li>
    <li>Do the RLE compression for the <a href="assets/img/letter-a.png" target="_blank">letter a </a> below as a class or in pairs (the first row is 1, 3, 1). Draw it in on the board or in the interactive pixel grid under Practice in the student side or copy the image to a projected document.<br/>
    <img src="../_static/assets/img/letter-a-RLE.png"/>
    </li>
    <li>Have students work in POGIL groups or pairs to complete the <a href="https://docs.google.com/document/d/1AkIwOQLTU4_TonpRh3LEqoLMXWiVdZ4AiYf1y-qWIEI/edit?usp=sharing" target="_blank">Image Representation worksheet</a>.  They could do these on paper or using the interactive pixel grid under Practice on the student side.</li>
    <li>Talk about how color is represented using RGB values, <a href="http://web.stanford.edu/class/cs101/image-rgb-explorer.html" target="_blank">RGB Color explorer</a>
    <!-- Old RGB Color Explorer Link  &lt;a href=&quot;http://introcomputing.org/image-rgb-explorer.html&quot; target=&quot;_blank&quot;&gt;RGB Color explorer&lt;/a&gt; -->
    </li></ul>
    <p>When finished, present a more detailed explanation of run-length encoding, storing images on computers, and other image compression techniques. Mention the trade-off in compression which is quality vs. file size and lossy vs. lossless compression (whether some data is lost when compressing, see this additional <a href="https://optimus.keycdn.com/support/lossy-vs-lossless/" target="_blank">resource</a> on lossy vs. lossless compression). There are several ways you can present this information. If you are new to teaching Mobile CSP, we suggest starting by having students watch the video lecture. As you become more familiar with the lesson and its content, you may decide to use the slides to give the lecture on your own, or guide students through reading the text-based lesson.
          </p><ul>
    <li>Have students watch the <a href="https://www.youtube.com/watch?v=xn3-BAiaJ1k" target="_blank">video</a> of the Mobile CSP version of the lecture</li>
    <li> Use the <a href="https://docs.google.com/presentation/d/1MmKmh7fJKCCfwGzA238VPXZYLkCZvIIUQZ9L-RIDEYQ/edit" target="_blank">slides</a> to give the lecture yourself.</li>
    <li> Have students read the <a href="https://docs.google.com/document/d/1Q4NinpY_-BLSjh9RVO1bD4apZYs4W93WbpX_nbas1Ec/edit" target="_blank">text-based version</a> of the lesson.</li>
    </ul>
    </li>
    <li>Optional Activities: If you have extra time, have students complete some of the "Other Activities" on the student side and watch some of the Still Curious videos (e.g.<a href=" https://youtu.be/Pc2aJxnmzh0" target="_blank">How Snapchat Filters work</a>).</li>
    <li><b>Rethink, Reflect, and/or Revise (10 minutes):</b> Have students complete the first two questions of their portfolio reflections in class and tell them to complete the last question for homework.</li>
    </ul>
    <div class="yui-wk-div" id="accordion">
    <h3 class="ap-classroom">AP Classroom</h3>
    <div class="yui-wk-div">
    <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
    <p><b>Suggested Topic Questions:</b></p><br/><ul><li><span style="font-weight: normal;">Topic 2.2 Data Compression<br/></span></li></ul></h4>
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
    <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.
        </p><ul>
    <li><i><b>Interactive Exercises:</b></i>
    <br/>Students should be able to use RLE to translate the numbers to images of letters in exercises 1 and 2.</li>
    <li><i><b>Portfolio Reflections:</b></i>
    <br/>Students should be able translate the binary in question 1 to ASCII to get the message "App Inventor ROCKS".
            <br/>They should, in question 2, be able to explain that JPEG compression is a lossy technique because some information is lost when this technique is used, but that these changes are not perceptible to the human eye and so do not lower the quality of the camera.
           <br/>Finally, in question 3, they should be able to describe how a binary sequence would be interpreted as a color when used as part an image, as a letter when part of a text message, and so on. 
            </li>
    </ul>
    </div>
    <h3 class="diff-practice">Differentiation: More Practice</h3>
    <div class="yui-wk-div">
    <p>To provide more practice with RLE, have students complete these <a href="http://csunplugged.org/wp-content/uploads/2014/12/unplugged-02-image_representation.pdf" target="_blank">CS Unplugged Worksheets</a> (pg. 17-18). [P3]<br/><br/>Mobile CSP Teachers Michael Wilkosz and Anthony Truss created a <a href="https://docs.google.com/document/d/1lYnZmoh-nGU33bymHyIc62cbgkX2SHNsBpsUtDW0-1Q/" target="_blank" title="">Run Length Encoding Image Project</a> in which students recreate their own image using a 16x16 grid in Adobe Illustrator. Alternatively, Paint, Gimp, or <a href="http://www.piskelapp.com" target="_blank" title="">PiskelApp.com</a> can be used to complete this assignment.<br/><br/>Mobile CSP Teachers Jessica Breed and Jenn Nelson created a similar <a href="https://goo.gl/photos/HXy1hBNujjwvFtMb9" target="_blank" title="">Pixel Art Project</a> that involves bringing the images to life using PostITs and posting them around the school building. </p>
    </div>
    <h3 class="diff-enrich">Differentiation: Enrichment</h3>
    <div class="yui-wk-div"><p>To extend students' understanding of RLE have them complete p. 19 of the <a href="http://csunplugged.org/wp-content/uploads/2014/12/unplugged-02-image_representation.pdf" target="_blank">CS Unplugged Worksheets</a> (pg. 17-18). [P3]</p></div>
    <h3 class="bk-knowledge">Background Knowledge: Run-Length Encoding</h3>
    <div class="yui-wk-div">
    <p>Simple black-and-white images such as fax images, as well as color pictures, have a lot of repetition in them. To reduce amount of the data needed to store and transmit images, computer scientists use a variety of <a href="http://en.wikipedia.org/wiki/Image_compression" target="_blank">image compression</a> techniques. The technique demonstrated in the video and used in this lesson is known as <b><i>run-length encoding</i></b>, or <b><i>RLE</i></b>. In this technique, the picture is converted into numbers by recording the length of alternating white and black pixels. This technique is well suited to images that have a lot of repetition in them. For example, fax images often have large blocks of white (e.g. margins) or black pixels (e.g. a horizontal line). Color pictures also have a lot of repetition in them. In practice, programmers choose a compression technique to best suit the image he or she is transmitting.</p>
    <p>From <i>CS Unplugged</i>: “If we didn't compress images it would take much longer to transmit pictures and require much more storage space. This would make it unfeasible to send faxes or put photos on a web page. For example, fax images are generally compressed to about a seventh of their original size, so without compression they would take seven times as long to transmit!  Photographs and pictures are often compressed to a tenth or even a hundredth of their original size (using a different technique). This allows many more images to be stored on a disk, and it means that viewing them over the web will take a fraction of the time.”</p>
    </div>
    <h3 class="bk-knowledge">Background Knowledge: Lossy vs Lossless Compression</h3>
    <div class="yui-wk-div"><p>There are generally two types of image compression
               techniques. Run-length encoding is
               a <b><i>lossless</i></b> technique, which means that the
               image is perfectly represented and no data are lost. It is
               the technique used in <b><i>TIFF</i></b> images. It is
               preferable for medical imaging, archival imaging, clip
               art, comics, and other applications.
    
             </p><p><i><b>Lossy compression</b></i> is not perfect. Some
               data may be lost. <b><i>JPEG</i></b> is an example of
               lossy compression. It is suitable for photographs and
               other applications where the loss of some data would be
        imperceptible. The <i>Still Curious</i> section of the Student
        lesson includes a <a href="https://www.youtube.com/watch?v=-yECdN-0tbo" target="_blank">short presentation</a> 
        on how JPEG works.  JPEG compression is based on an algorithm that
        uses the cosine function.  But the presentation leaves out most of 
        the math details.  Here is a link to the <a href="https://docs.google.com/presentation/d/1QG8IBtYjFIfQCcSqC61kwVs4ZEciFRBSK1VlJFHP_Gs" target="_blank">slides</a>.
    
             </p><p>The <i><b>trade-off</b></i> is between storage required
               for the image vs. fidelity or quality. If a lot of
               compression is required -- perhaps because of transmission
               requirements -- a lossy technique may be preferred.
           </p></div>
    </div> <!-- accordion -->
    <div class="pd yui-wk-div">
    

Professional Development Reflection
------------------------------------

.. raw:: html

    <p>
    <p>Discuss the following questions with other teachers in your professional development program.</p>
    <ul>
    <li>How does this lesson help students toward the enduring understanding that all digital data can be represented by a variety of abstractions built upon binary sequences?</li>
    <li>What might be some other trade-offs that students could connect to that would reinforce the enduring understanding that there are trade-offs when representing information as digital data? </li>
    <li>How does this lesson develop students' computational thinking practices, particularly their analysis and problem solving skills and their ability to use abstractions?</li>
    </ul>
    <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
    <p>
.. poll:: mcsp-3-3-1
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

 
.. fillintheblank:: mcsp-3-3-2

    What questions do you still have about the lesson or content presented? |blank|

    - :/.*/i: Thank you. We will review these to improve the course content.
      :x: Thank you. We will review these to improve the course content.


.. raw:: html

    <div id="bogus-div">
    <p></p>
    </div>

    </div>
    </div>