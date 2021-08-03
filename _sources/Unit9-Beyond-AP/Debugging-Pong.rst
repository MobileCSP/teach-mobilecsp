.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Debugging Pong (Optional) 
==========================

.. raw:: html

	<!-- Copy these lines to the top of the lesson's HTML code.  -->
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/tipped.js"></script>
	<script type="text/javascript" src="assets/lib/Framework2020.js"></script>
	<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<script>
	$(document).ready(function() {
	     generateFrameworkTable(EKmapping['9.10']);
	     generateHovers();
	 });
	
	</script>
	
	<p class="overview"><a target="_blank" href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/Debugging-Pong.html">This lesson</a> revisits the Pong game. Now that students understand how it should work correctly, they find bugs in a game that doesn't work correctly. Before, the listen to a presentation that describes what debugging is as well as the different types of bugs in programs. The lesson reinforces their understanding of what it means for a program to work correctly.</p>
	
	<table border id="genTable" class="framework" width="100%"></table>
	
	<div class="pd yui-wk-div">
	 <h3>Professional Development</h3> 
	 <p><b>The Student Lesson:</b> Complete the activities for <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/Debugging-Pong.html" target="_blank">Mobile CSP Lesson 9.10 Debugging Pong</a>.
	 </p>
	</div>
	
	
	<h3>Materials</h3>
	<p></p>
	<ul>
	  <li><a href="https://docs.google.com/presentation/d/1VJzIXEueLY5EmGm5VPpKEJg07P3xxYJfa5rTwGTnVGA/edit?usp=sharing" target="_blank">Slides on Debugging</a></li>
	  <li>Projection system and computer lab</li>
	  <li>Android devices or emulator</li>
	</ul>
	
Learning Activities
-----------------------

.. raw:: html

	
	<h3 id="est-length">Estimated Length: 45 minutes</h3>
	<p></p>
	
	<ul>
	  <li><b>Hook/Motivation (10 minutes):</b> (Think-Pair-Share) Show a sample of App Inventor code to students and ask them to write down what they think the code is supposed to do and what it actually does. Have them share answers with a partner and with the class. The example below is from a Space Invaders game with a Sprite for one of the invaders, which moves similar to the Android in AndroidMash. The MyCanvas property should be Width instead of BackgroundImage. For this example, make sure everyone in the class knows what happens in the Space Invaders game.<br>
	    <a href="../_static/assets/img/spaceinvadersUI.png" target="_blank"><img src="../_static/assets/img/spaceinvadersUI.png" class="yui-img" height="350"></a>
	    <a href="../_static/assets/img/spaceinvadersCode.png" target="_blank"><img src="../_static/assets/img/spaceinvadersCode.png" class="yui-img" width="650"></a>
	 </li>
	 <li><b>Experiences and Explorations (25 minutes):</b>
	   <ul>
	     <li><b>Explanation (10 minutes):</b> Either use the slides to present concepts on debugging or have students watch the video.</li>
	     <li><b>Debugging (15 minutes):</b> Have students download the Pong with Bugs app and try to find the three errors. The students should do any necessary tests to determine what the bugs may be. Point out that their knowledge of how the Pong Game works will help them find any errors. The students should make incremental corrections. After attempting to fix one bug, the students should test the app before continuing.</li>
	   </ul>
	 </li>
	 <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Review the debugging strategies and syntax vs. semantic errors. Have students complete the interactive exercises and portfolio reflection</li>
	</ul>
	
	<div id="accordion">
	<h3 class="ap-classroom">AP Classroom</h3>
	 <div class="yui-wk-div">
	 <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
	   <h4>Suggested Topic Questions:</h4>
	</div>
	<h3 class="assessment">Assessment Opportunities</h3>
	 <div>
	   <p>You can examine students’ work on the interactive exercise and their reflection portfolio entries to assess their progress on the following learning objectives. If students are able to do what is listed there, they are ready to move on to the next lesson.</p>
	   <ul>
	     <li><i><b>Interactive Exercises:</b></i> </li>
	     <li><i><b>Portfolio Reflections:</b></i>
	         <br>LO X.X.X - Students should be able to ...
	     </li>
	     <li><i><b>In the XXX App, look for:</b></i>
	     </li>
	     <li><a href="https://docs.google.com/a/css.edu/document/d/1BuRpe42HqQwfUQRYhE1889fK8HJ_sCU6q0xC9DuE15s/edit#heading=h.8r6d94t48ft9" target="_blank">Solutions to Pong with Bugs exercise</a></li>
	   </ul>
	 </div>
	 
	 <h3 class="diff-practice">Differentiation: More Practice</h3>
	 <div>
	   <p>If students are struggling with the lessons, they should explain in their own words how the app is supposed to work and identify what is not working. If needed, they can review the code from the completed Pong game.</p>
	 </div>
	 
	 <h3 class="diff-enrich">Differentiation: Enrichment</h3>
	 <div>
	   <p>Students can introduce their own bug to the Pong game and then have a partner try to debug it.</p>
	 </div>
	
	
	 <h3 class="tips">Teaching Tips: Debugging</h3>
	 <div>
	   <p>Debugging is a very common programming practice that should be emphasized throughout the course. However, in order for students to be effective debuggers, they must first understand how the program is supposed to work. If they are struggling, have them describe out loud how the program should work and then identify what is not working correctly.</p>
	 </div>
	
	 
	</div> <!-- accordion -->
	
	
	
	<div class="pd yui-wk-div">

Professional Development Reflection
----------------------------------------------

.. raw:: html

	 <p>Discuss the following questions with other teachers in your professional development program.</p>
	 <ul>  
	   <li><div class="hover eu yui-wk-div" data-id=""></div></li>  <!-- for an EU -->
	 </ul>
	 
	 <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
	 <question quid="6241370977075200" weight="0" instanceid="fuNQwmAbe7f2"></question>
	 <question quid="4687848556986368" weight="0" instanceid="3kQHQSwyljT6"></question>
	
	</div>
