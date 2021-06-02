.. raw:: html 

    <a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>

Socially Aware App: Broadcast Hub Tutorial 
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
	     generateFrameworkTable(EKmapping['9.13']);
	     generateHovers();
	 }); 
	
	</script>
	
	<p class="overview"><a target="_blank" href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=111" title="">This lesson</a> uses the App Inventor ActivityStarter component to set up a mini social network using the concept of a hub — a network component that sends a message received to all other devices connected to the hub. It reinforces the enduring understandings that computing can be used to solve problems (spreading a message among a group), and that computing innovations affect (and are influenced by) social contexts. If phones are available, the hub can be set up to use texting instead of email.</p>
	
	<table border id="genTable" class="framework" width="100%"></table> 
	
	<div class="pd yui-wk-div">
	 <h3>Professional Development</h3> 
	 <p><b>The Student Lesson:</b> Complete the activities for <a href="https://course.mobilecsp.org/mobilecsp/unit?unit=25&amp;lesson=111" target="_blank" title="">Mobile CSP Lesson 9.13: Broadcast Hub Tutorial</a>. 
	 </p>
	</div>
	
	<h3>Materials:</h3>
	<p></p>
	<ul>
	 <li>Computer lab with projection system</li>
	 <li>Android devices or emulator</li>
	 <li><a href="https://docs.google.com/document/d/1vb3jKCSDLgb8BJvg90zH3tCla9PT2AhpZ3GiFznCzsY/" target="_blank" title=""><a href="https://docs.google.com/a/css.edu/document/d/1iRM1Ku59mhovuwEvQSY8cY0q1e9YViK56gF6vnl-_jg/edit" target="_blank">Solutions</a></a></li>
	</ul>
	
Learning Activities
-----------------------

.. raw:: html

	<h3 id="est-length">Estimated Length: 90 minutes (45 minutes without Enhancements</h3>
	<p><i>Note: This app requires an email program, but could also be completed using texting if students have a phone with SMS service.</i></p>
	
	<ul>
	 <li><b>Hook/Motivation (10 minutes):</b> Have students work in small groups to brainstorm and draw different methods of "getting the message out". Prompt them to think about how this might happen for their athletic or club groups, at their church, how information spreads on Facebook, among students at school, etc. They might come up with examples that look like webs, like trees (i.e. phone trees), or even hubs - where one person sends out the message to the entire group.</li>
	 <li><b>Experiences/Explorations (60 minutes):</b> Describe what a hub is (<a href="http://www.webopedia.com/TERM/H/hub.html" target="_blank">Webopedia definition</a>). Walk the students through the Broadcast Hub tutorial, emphasizing the points below. Then, have&nbsp;students complete the enhancements found at the bottom of the tutorial. If students need assistance or want to check their coding, have them review the solutions.
	   <ul>
	     <li>Have students identify the events in the app that need to be coded (the two button click events)</li>
	     <li>For each event, have them describe what steps need to occur in the code (an algorithm)</li>
	     <li>Review the components of an email message (to address, subject, message) and have them identify where in the UI or code that information will be stored. Then show them how the DataURI property of the ActivityStarter represents the email message. Note: the ampersands are really just about joining information together. Students should be careful, though, not to include extra spaces. (Spaces are only allowed in the subject and message, not in other areas.)</li>
	     <li>Walkthrough the broadcastMessage procedure, highlighting the difference between a local and global variable that local is appropriate here because it's only used in this procedure and not in other areas of the code.</li>
	     <li>Review the use of the for-each loop with a list, used in this case to concatenate (join) all the email addresses with a comma</li>
	   </ul>
	 </li>
	 <li><b>Rethink, Reflect, and/or Revise (20 minutes):</b> Watch this PBS NewsHour Video: <a href="http://youtu.be/zGCxiD4qREM" target="_blank">Mobile Phone Usage in Explodes in Africa, Spurring Innovation</a>, and discuss the similarities and differences between their experience and the experiences of those in the video. Have the students try to complete the interactive exercises and complete a reflection in their portfolio. Any unfinished work should be assigned as homework.</li>
	</ul>
	
	
	<div id="accordion" class="yui-wk-div">
	<h3 class="ap-classroom">AP Classroom</h3>
	 <div class="yui-wk-div">
	 <p>The College Board's <a href="http://myap.collegeboard.org" target="_blank" title="AP Classroom Site">AP Classroom</a> provides a question bank and Topic Questions. You may create a formative assessment quiz in AP Classroom, assign the quiz (a set of questions), and then review the results in class to identify and address any student misunderstandings.The following are suggested topic questions that you could assign once students have completed this lesson.</p>
	   <h4>Suggested Topic Questions:</h4>
	</div>
	 
	 <h3 class="diff-practice">Differentiation: More Practice</h3>
	 <div class="yui-wk-div">
	   <p>If students are struggling with lesson concepts, have them review the following resources:</p>
	   <ul>
	     <li><a href="http://www.webopedia.com/TERM/H/hub.html" target="_blank">Webopedia hub definition</a></li>
	     <li>AI2 Documentation: <a href="http://ai2.appinventor.mit.edu/reference/components/social.html#Texting" target="_blank">Texting component</a></li>
	   </ul>
	 </div>
	 
	
	 
	</div> <!-- accordion -->
	
	<div class="pd yui-wk-div">

Professional Development Reflection
-----------------------

.. raw:: html

	 <p>Discuss the following questions with other teachers in your professional development program.</p>
	 <ul>  
	   <li>Compare the Broadcast Hub app to the No Texting While Busy app. How do these two tutorials differ in addressing the enduring understandings regarding computing and communication? [<div class="hover eu yui-wk-div" data-id="7.1">7.1</div>, <div class="hover eu yui-wk-div" data-id="7.4">7.4</div>]</li>  <!-- for an EU -->
	 </ul>
	 
	 <!-- These are the PD exit slips.  We should have corresponding exit slips for use after the classroom lesson. -->
	 <question quid="4620077865369600" weight="0" instanceid="4iFwOgOoKfxo"></question>
	 <question quid="6225708439306240" weight="0" instanceid="ykr083FNVgel"></question>
	
	</div>
	
