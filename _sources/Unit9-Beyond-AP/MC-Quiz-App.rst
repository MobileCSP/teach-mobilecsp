.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Multiple Choice Quiz App: List of Lists (Optional) 
====================================================

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
	     generateFrameworkTable(EKmapping['9.11']);
	     generateHovers();
	 });
	
	</script>
	
	
	<p class="overview"><a target="_blank" href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/MC-Quiz-App.html" title="">This lesson</a> introduces the concept of a <i>list of lists</i>, where each item in the outer list (instead of being a number, boolean, or text value) is another list, or sublist. Students will also use a ListPicker component to display the answer choices (the sublist) to the user in a user-friendly way.</p>
	
	<table border id="genTable" class="framework" width="100%"></table>
	
	<div class="pd yui-wk-div">
	 <h3>Professional Development</h3> 
	 <p><b>The Student Lesson:</b> Complete the activities for 
	   <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/MC-Quiz-App.html" target="_blank" title="">Mobile CSP Lesson 9.11 Multiple Choice Quiz App: List of Lists</a>.
	 </p>
	</div>
	
	
	
	<!--
	<h2>2. Review the Lesson Plan </h2>
	<h3>Content Standards (CS)</h3>
	<table>
	  <tbody><tr>
	      <th width="33%">Learning Objectives<br>(What students must be able to do)</th>
	      <th>Essential Knowledge<br>(What students need to know)</th>
	  </tr>
	  <tr>
	      <td>1.2.3 Create a new computational artifact by combining or modifying existing artifacts.</td>
	      <td>1.2.3B Computation facilitates the creation and modification of computational artifacts with enhanced detail and precision.</td>
	   </tr>
	  <tr>
	      <td>3.1.1 Use computers to process information, find patterns, and test hypotheses about digitally processed information to gain insight and knowledge. [P4]</td>
	      <td>3.1.1A Computers are used in an iterative and interactive way when processing digital information to gain insight and knowledge. </td>
	   </tr>
	  <tr>
	      <td>5.5.1 Employ appropriate mathematical and logical concepts in programming. [P1]</td>
	      <td>5.5.1H Computational methods may use lists and collections to solve problems.
	      <br>5.5.1J Basic operations on collections include adding elements, removing elements, iterating over all elements, and determining whether an element is in a collection.</td>
	   </tr>
	</tbody></table>
	
	<h3>Student Objectives (Knowledge and Skills)</h3> 
	<p></p>
	<ul>
	  <li>Use a ListPicker component to choose items from a predefined list.</li>
	  <li>Combine list within lists to make an interactive multiple choice quiz with text and images.</li>
	</ul>
	
	
	-->
	
	<h3>Materials</h3>
	<p></p>
	<ul>
	  <li>Computer lab</li>
	  <li>Android devices or emulator</li>
	</ul>
	
	
Learning Activities
-----------------------

.. raw:: html

	<h3 id="est-length">Estimated Length: 45 minutes</h3>
	<p></p>
	<ul>
	 <li><b>Hook/Motivation (10 minutes):</b> Ask students: Why was the Presidents Quiz app difficult for some users to determine the correct answer?  <i>Explanation:</i> Describe the student learning goals for today’s lesson. Refer to the Learning Objectives and have students take note that in today’s lesson the use of Lists will be heavily emphasized. In order to enhance the Presidents Quiz app and make it more challenging for users, a list of lists will be created to make multiple choice questions with different answer choices for each question.</li>
	
	 <li><b>Experiences and Explorations (30 minutes):</b> Have the students complete the List of Lists tutorial on their own. Make sure to identify new variables that can hold more than one value, a List of Lists.</li>
	 <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Discuss as a class how a list of lists was used and created in the tutorial. Have students complete a reflection in their portfolio (this may be assigned as homework). Have students try the interactive exercises, either individually or as a class.</li>
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
	   </ul>
	 </div>
	 
	 <h3 class="diff-practice">Differentiation: More Practice</h3>
	 <div>
	   <p>If students are struggling with lesson concepts, have them review the following resources:</p>
	   <ul>
	     <li><a href="http://appinventor.mit.edu/explore/ai2/support/blocks/lists.html" target="_blank">AI2 Documentation on Lists</a></li>
	     <li><a href="http://appinventor.mit.edu/explore/ai2/support/concepts/lists.html" target="_blank">AI2 Concept on Using Lists</a></li>
	   </ul>
	 </div>
	 
	 <h3 class="diff-enrich">Differentiation: Enrichment</h3>
	 <div>
	   <p>Have students modify the app they built in the President's Quiz app projects so that it also uses multiple choice questions with a list of lists and a ListPicker.</p>
	 </div>
	
	 <h3 class="bk-knowledge">Background Knowledge: Lists</h3>
	 <div>
	   <ul>
	     <li><a href="http://appinventor.mit.edu/explore/ai2/support/blocks/lists.html" target="_blank">AI2 Documentation on Lists</a></li>
	     <li><a href="http://appinventor.mit.edu/explore/ai2/support/concepts/lists.html" target="_blank">AI2 Concept on Using Lists</a></li>
	   </ul>
	 </div>
	
	 
	</div> <!-- accordion -->
	
	<div class="pd yui-wk-div">

Professional Development Reflection
-------------------------------------

.. raw:: html

	 <p>Discuss the following questions with other teachers in your professional development program.</p>
	 <ul>  
	   <li><div class="hover eu yui-wk-div" data-id=""></div></li>  <!-- for an EU -->
	 </ul>
	 
	 <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
	 <question quid="5317607397785600" weight="0" instanceid="tVoltYWKyStY"></question>
	 <question quid="5662758485884928" weight="0" instanceid="9uE29BK0zw8E"></question>
	</div>
