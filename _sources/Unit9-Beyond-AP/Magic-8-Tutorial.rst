.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

Magic 8 Ball Tutorial and Projects (Optional)
=============================================

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
	     generateFrameworkTable(EKmapping['9.05']);
	     generateHovers();
	 }); 
	
	</script>
	
	<p class="overview"><a target="_blank" href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/Magic-8-Tutorial.html" title="">This lesson</a> includes both a tutorial that leads the student through the creation of a mobile version of the classic "Magic 8 Ball" game and several programming challenges that students will work in pairs to solve.  The Magic 8 Ball app simulates the Magic 8 Ball game:  when the user asks a question and shakes the device the app will respond with a random prediciton.  The tutorial shows how to use App Inventor's <i>Accelerometer</i> to detect the device's motion and its <i>Text to Speech</i> component to convert text to speech.  Two of the programming tasks involve the use of App Inventor's <i>Clock</i> component and can be quite challenging.  A solution to those is provided in the lesson plan.  In addition to promoting the enduring understanding about the importance of collaboration in designing and writing programs, this lesson also introduces an important new programming abstraction, a <i>list</i>, which is used to store a collection of items in the computer's memory.  It thus also reinforces the enduring understanding that programming is facilitated by appropriate abstractions. 
	
	<table border id="genTable" class="framework" width="100%"></table>
	
	<div class="pd yui-wk-div">
	 <h3>Professional Development</h3>  
	 <p><b>The Student Lesson: </b> Complete the activities for 
	   <a href="https://runestone.academy/runestone/books/published/mobilecsp/Unit9-Beyond-AP/Magic-8-Tutorial.html" target="_blank" title="">Mobile CSP Lesson 9.5: Magic 8 Ball Tutorial and Projects</a>.
	 </p>
	</div>
	
	<h3>Materials</h3>
	<ul>
	  <li>Computer lab and projection system</li>
	  <li>Android devices - <i>note that this tutorial uses the Accelerometer, which is not part of the emulator and so requires a device</i>. If you are only using an emulator, instead of the Accelerometer, create a button that when clicked does the same thing as the phone being shaken.</li>
	</ul>
	
Learning Activities
-----------------------

.. raw:: html

	<h3 id="est-length">Estimated Length: 90 minutes</h3>
	
	<h3>Day 1 - Magic 8 Ball Tutorial (45 minutes)</h3>
	<p></p>
	<ul>
	  <li><b>Hook/Motivation (10 minutes):</b> "What is a Magic 8-Ball?" Have they ever used one? What does it do? Is it possible to make a virtual Magic 8-Ball? A Magic 8-Ball is a fortune-telling toy. Ask it a Yes or No question, shake it, and it will make a prediction.
	    <ul>
	      <li>Wikipedia has a nice explanation of a <a href="http://en.wikipedia.org/wiki/Magic_8-Ball" target="_blank">Magic 8-Ball</a>.</li>
	      <li>The Three Stooges used a Magic 8-Ball in their "You Nazty Spy" series from the 1940s. See at the 1:00 minute mark of <a href="http://www.youtube.com/watch?v=MLLc5_YBpy8&amp;t=1m" target="_blank">this video clip</a>. (Can't find a free online version in English.)</li>
	      <li>Play with <a href="http://www.ask8ball.net/" target="_blank">Ask 8 Ball</a>, a free online version of the game.</li>
	    </ul>
	 </li>
	  <li><b>Experiences and Explorations (25 minutes):</b> Describe the student objectives for today’s lesson. In today's lesson another abstraction concept, the concept of defining a list, will be introduced. Lead the students through the Magic 8-Ball tutorial. Allow faster students to follow the tutorial on their own. If using the Magic 8-Ball Template identify new components used in this app as you discuss the design of the UI with the students and walk students through the coding of the app. You can also choose to use the Magic 8-Ball Media Only Template and create the UI from scratch with the students.
	  <br>Be sure to discuss the Accelerometer component; creating a list and how a random item from a list can be chosen. This includes identifying an empty list, a list index, and the length of list; and the Text-to-Speech component.</li>
	 <li><b>Rethink, Reflect and/or Revise (10 minutes):</b>  Have the students try to complete the interactive exercises and complete a reflection in their portfolio.</li>
	</ul>
	
	<h3>Day 2 - Magic 8 Ball Projects (45 minutes)</h3>
	<p></p>
	<ul>
	  <li><b>Hook/Motivation (10 minutes):</b> Discuss possible enhancements to the Magic 8-Ball app using the Think-Pair-Share technique.</li>
	  <li><b>Experiences and Explorations (25 minutes):</b> Students work in pairs on enhancements to Magic 8-Ball; teacher answers questions.</li>
	  <li><b>Rethink, Reflect and/or Revise (10 minutes):</b> Students make a new entry in their portfolios. Have the students describe the modifications and enhancements that they made to the Magic 8-Ball app. Also ask the students to reflect on their programming experience. See the Magic 8-Ball mini projects solutions. Discuss what issues the students encountered while modifying the Magic 8-Ball app. Check students understanding using the interactive exercises.</li>
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
	     <li><i><b>In the Magic 8 Ball App, look for:</b></i>
	     </li>
	   </ul>
	   
	   <p><b>Solution to the Challenges:</b> Here is one solution to the two challenge problems given in this lesson. It involves using both the <i>Clock</i> and the <i>SpeechRecognizer</i>.  The logic behind this algorithm can be a bit tricky.  It involves coordinating the behavior of three separate blocks.
	<br>
	First, when the device is shaken, the Sound is played and the SpeechRecognizer is started.  Notice also that the label that displays the answer is blanked out.  When the SpeechRecognizer is started, it will prompt the user, which will stop any further blocks from firing.
	<br>
	<img src="../_static/assets/img/WhenShaking.png" width="400">
	<br>
	When the user stops speaking, the SpeechRecognizer's AfterGettingText block will fire automatically.  This is where you would repeat what the user said (optional) and enable the Timer.  This will start the Timer ticking.  To provide a sufficient delay, the Timer interval is set to 2000 milliseconds.
	<br>
	<img src="../_static/assets/img/AfterGettingText.png" width="400">
	<br>
	Finally, when the Clock.Timer  block fires, you want to get and speak the prediction and 
	stop the Timer. 
	<br>
	<img src="../_static/assets/img/WhenTimer.png" width="400">
	<br>Of course, this is only one possible solution to the problem.  There are others.
	</p></div>
	 
	 <h3 class="diff-practice">Differentiation: More Practice</h3>
	 <div>
	   <ul>
	     <li><a href="http://appinventor.mit.edu/explore/ai2/support/blocks/lists.html" target="_blank">AI2 Documentation on Lists</a></li>
	     <li><a href="http://ai2.appinventor.mit.edu/reference/components/userinterface.html#ListPicker" target="_blank">AI2 Documentation on ListPicker</a></li>
	   </ul>
	 </div>
	 
	 <h3 class="diff-enrich">Differentiation: Enrichment</h3>
	 <div>
	   <p>ListPicker components can be initialized from a list variable using the Elements property (instead of ElementsFromString). Have students change their code to make use of a list for the Speak, Sound, Silent options.
	 </p></div>
	
	 <h3 class="bk-knowledge">Background Knowledge: Lists and ListPicker</h3>
	 <div>
	   <p><b><i>Lists</i></b> are frequently used to store multiple pieces of similar data, instead of multiple variables. AppInventor.org has a number of <a href="http://www.appinventor.org/content/howDoYou/RecordingInfo" target="_blank">How Do You? mini-lessons</a> on lists that will provide more background on how lists are used, as well as a chapter in the <a href="http://www.appinventor.org/bookChapters/chapter19.pdf" target="_blank">AppInventor 2 book</a>. We will be using lists more throughout the course and learn some of those concepts in upcoming lessons.</p>
	   <p><b><i>ListPickers</i></b> are a common and useful UI component in mobile apps as they save space on smaller, mobile screens. Key events and properties are summarized in the table below.</p>
	   <table>
	     <tbody><tr style="background-color: grey">
	       <th>Event or Property</th>
	       <th>Description</th>
	     </tr>
	     <tr>
	       <td><b>Event: BeforePicking</b></td>
	       <td>Triggered when the ListPicker is clicked, use to set the list dynamically</td>
	     </tr>
	     <tr>
	       <td><b>Event: AfterPicking</b></td>
	       <td>Triggered after the user makes a choice, use to respond to a choice</td>
	     </tr>
	     <tr>
	       <td><b>Property: Elements</b></td>
	       <td>A list of choices</td>
	     </tr>
	     <tr>
	       <td><b>Property: ElementsFromString</b></td>
	       <td>A comma-separated string of choices (EX: choice1, choice2, choice3)</td>
	     </tr>
	     <tr>
	       <td><b>Property: Selection</b></td>
	       <td>The user's choice</td>
	     </tr>
	     <tr>
	       <td><b>Property: SelectionIndex</b></td>
	       <td>The position of the user's choice (first item in the list is 1)</td>
	     </tr>      
	   </tbody></table>
	 </div>
	 
	</div> <!-- accordion -->
	
	
	<div class="pd yui-wk-div">

Professional Development Reflection
----------------------------------------------

.. raw:: html

	 <p>Discuss the following questions with other teachers in your professional development program.</p>
	 <ul>    
	   <li>How does this lesson help students toward the enduring understanding that programming is facilitated by appropriate abstractions, in this case a <i>list</i>?  
	     <div class="hover eu yui-wk-div" data-id="5.3">[EU 5.3]</div>?
	   </li>
	 </ul>
	 
	 <p>
	   <question quid="6344244100857856" weight="0" instanceid="MjZhsOsiLWIh">
	   </question>
	   <question quid="6118245606096896" weight="0" instanceid="ah6hC7XI2kC8">
	   </question>
	 </p>
	</div>
