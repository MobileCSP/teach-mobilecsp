.. raw:: html 

   <div class="logo-header"  id="teacher-logo"  > <img class="align-center" src="../_static/Mobile_CSP_Logo_White_transparent.png" width="250px"/> </div>

AP CS Principles Exam Prep 
==========================

.. raw:: html

	<!-- Copy these 5 lines to the top of the lesson's HTML code.  -->
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	<link rel="stylesheet" href="https://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
	
	<!--<style>
	tr, td {
		border: 1px solid black;
		text-align: center;
	}
	</style>-->
	
	<!-- remove unnecessary scripts and stylesheets
	<script type="text/javascript" src="assets/lib/lessons/tipped.js"></script>
	<script type="text/javascript" src="assets/lib/lessons/framework.js"></script>
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/tipped.css">
	<link rel="stylesheet" type="text/css" href="assets/lib/lessons/lessons.css">
	-->
	
	<script>
	 $(function() {
	   $( "#accordion" ).accordion({
	     collapsible: true,
	     active: false,
	     heightStyle: "content",
	     icons: false
	   });
	 });
	</script>
	<script>
	 $(function() {
	   $( "#accordion2" ).accordion({
	     collapsible: true,
	     active: false,
	     heightStyle: "content",
	     icons: false
	   });
	 });
	</script>
	
Sample 1 - 2017's Sample A
----------------------------------------------

.. raw:: html

	   <div id="accordion" class="yui-wk-div">
	
	<h3>Row 1: Developing a Program with a Purpose (Video and Response 2A)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) The video demonstrates the running of at least one feature of the program submitted. </p>
			<p>AND</p> 
			<p>B.) The response (audio narration or written response) identifies the purpose of the program 
			(what the program is attempting to do).</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>A.) The video is a continuous running of the program that demonstrates several features 
			(i.e. log in, review, add entries) in under a minute.</p>
			<p>AND</p>
			<p>B.) The response (in this case the audio narration) matches the video and indicates that the 
			purpose of the program is “to allow users to have an app where they can privately journal about their day”</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>The video and narration are well planned out and executed.  It is simple and yet thoroughly explains the app.
	     The two things to remember the difference between are purpose and function.  Purpose is the intended goal or 
	     objective of the program.  Function is how the program works.</p>
	<h4>Student Response</h4>
		<gcb-youtube videoid="https://www.youtube.com/watch?v=suZL5PnpD8Y" instanceid="aSSDfX1wPX3Z"></gcb-youtube><br><p>2a. Narration in video</p>
	</div>
	
	<h3>Row 2: Developing a Program with a Purpose (Response 2B)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Describes or outlines steps used in the incremental and iterative development process to create the entire program.</p>
		</td>
		<td>
			<p>0</p>
		</td>
		<td>
			<p>The response only describes the development at two specific points in time. The response lacks discussion of the overall 
	             development process of the app. A good response would describe the steps taken to develop the program including information 
	             about the testing, debugging, and refinement of the program once the initial code was written.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>Students should focus on conveying the overall process of the app development.  Clearly defining the start and finish of the process while
	     touching on important milestones along the way is very important to this response.</p>
	<h4>Student Response</h4>
		<p>2b. Being unfamiliar with Firebase’s structure, I encountered a problem while programming when I tried to include a 3rd Firebase database.
	         Upon the addition of the component and the corresponding coding elements, my app could no longer be packaged or loaded onto a device for
	         testing. My app would always crash while loading. Unable to find a clear syntax error, I resolved the issue by debugging and deleting
	         portions of the code until the app would finally successfully load and then reprogramming the deleted portions of code. Another difficulty
	         I encountered was transferring variables across screens in order to access the correct user’s data. Opening a new screen in App Inventor
	         would clear the values of the variable on the device, which would render them unusable on the next screen. I resolved this independently
	         by assembling the contents of each screen into its own arrangement, and utilizing the .visible property of these arrangements to make
	         them appear and disappear, providing the illusion of multiple screens and allowing the accessed variable values to be consistent across
	         all “screens”.</p>
	</div>
	
	<h3>Row 3: Developing a Program with a Purpose (Response 2B)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) Specifically identifies at least two program development difficulties or opportunities.  </p>
			<p>AND</p> 
			<p>B.) Describes how the two identified difficulties or opportunities are resolved or incorporated.</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p></p><p>A.) The response describes two program development difficulties/opportunities</p>
			<p>AND</p>
			<p>B.) explains how each was resolved.</p>
			<p>The first difficulty is that when including a third Firebase database, the program could no longer be packaged or loaded onto a device
	             for testing. <i>This is resolved by deleting portions of the code until the app worked, and then adding back in the deleted
	             portions.</i></p>
			<p>The second difficulty is transferring variables across screens. <i>This is resolved by using the visible property of these 
	             arrangements to make them appear and disappear, providing the illusions of multiple screens.</i></p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>Students should explicitly label their opportunities or difficulties as done in this example.  Adding the sentence structures “the first…”
	     and “the second…” also makes it unmistakeable for the grader to identify.  The way the student points out the resolution of the difficulties is
	     spot-on by specifically using the phrase “I resolved”.</p>
	<h4>Student Response</h4>
		<p>2b. Being unfamiliar with Firebase’s structure, I encountered a problem while programming when I tried to include a 3rd Firebase database.
	         Upon the addition of the component and the corresponding coding elements, my app could no longer be packaged or loaded onto a device for
	         testing. My app would always crash while loading. Unable to find a clear syntax error, I resolved the issue by debugging and deleting
	         portions of the code until the app would finally successfully load and then reprogramming the deleted portions of code. Another difficulty
	         I encountered was transferring variables across screens in order to access the correct user’s data. Opening a new screen in App Inventor
	         would clear the values of the variable on the device, which would render them unusable on the next screen. I resolved this independently
	         by assembling the contents of each screen into its own arrangement, and utilizing the .visible property of these arrangements to make
	         them appear and disappear, providing the illusion of multiple screens and allowing the accessed variable values to be consistent across
	         all “screens”.</p>
	</div>
	 
	<h3>Row 4: Applying Algorithms (Response 2C)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Selected code segment implements an algorithm.</p>
			<p>Indicated by placing an oval around the specific piece of code in the entire program code section.</p> 
			<p>If using the template, a screenshot is provided directly with the response.</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>By the definition of an algorithm, the selected code segment does implement an algorithm.<br>The main algorithm pictured here is 
	             the AccountDB.GotValue block. For easy reference, the response also includes screenshots of two sub-algorithms (algorithms included 
	             in the main algorithm). In this case, both sub-algorithms are procedures.<br>The written response matches the selected code.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>By providing a screenshot of the algorithm, the student simplified the process of identifying the algorithm.  Students need to be very careful 
	     to select an algorithm that fills the requirements for <em>both</em> rows 5 and 6.</p>
	<h4>Student Response</h4>
		<p>2c.<br>
	         <img src="../_static/assets/img/CreateSample12C.png" class="yui-img" title="" alt=""><br>
	         <img src="../_static/assets/img/CreateSample12C2.png" class="yui-img" title="" alt="">
	         <img src="../_static/assets/img/CreateSample12C3.png" class="yui-img" title="" alt=""></p>
	</div>
	 
	<h3>Row 5: Applying Algorithms (Response 2C)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) Selected code segment implements an algorithm that uses mathematical or logical concepts.</p>
			<p>AND</p> 
			<p>B.) Explains how the selected algorithm functions </p>
	         	<p>AND</p> 
	           <p>C.) Describes what the selected algorithm does in relation to the overall program.</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>A.) The selected code segment in this case is the main algorithm - the AccountDB.GotValue block. It satisfies the math/logic 
	             requirement because it uses an If/Else statement with Boolean conditions which counts as logic.</p>
			<p>AND</p>
			<p>B.) The response explains how the algorithm functions by stating it “examines the tag and values sent back in order to properly 
	             redirect the program to either proceed with a login or create account procedure”. </p>
			<p>AND</p>
	         	<p>C.) The response describes what the algorithm does in relation to the overall purpose of the program (stores user data).</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>Students should take the time to explicitly describe the logical or mathematical concepts used in the design of the algorithm. This statement,
	     “redirect the program to either proceed with a login or create account procedure.” talks about the selection process, but could put more emphasis
	     on it being the logical part of the algorithm.
	Great use of the phrase “the algorithm examines” points out the function of it.  To show the relation to overall program, this example uses another 
	     great sentence structure  “...is an important algorithm as it handles...”</p>
	<h4>Student Response</h4>
		<p>2c. As my program uses Firebase databases to store user data, AccountDB.GotValue is an important algorithm as it handles all data retrieved 
	         from the account database such as users and passwords. Because Firebase data requests are handled asynchronously to the program, it is 
	         necessary that when data is sent back from Firebase, the algorithm examines the tag and values sent back in order to properly redirect the 
	         program to either proceed with a login or create account procedure.&nbsp; One of the integrated algorithms is the procedure called 
	         loginProcedure (above). When called, the procedure loginProcedure will login in the user and load up the user’s diary entries if the correct 
	         password is entered. Otherwise, an error message will appear and the user will have to try again. 
		The procedure createAccount shown above is another integrated algorithm that helps create a user’s account and mark the designated locations for 
	         the user’s data in Firebase given that they had provided a valid password and an unique username. The integration of the two procedures 
	         createAccount and loginProcedure helps the overall algorithm perform and regulate the core functions of the login screen of creating accounts 
	         and logging in.</p>
	</div>
	 
	<h3>Row 6: Applying Algorithms (Response 2C)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>• A.) Selected code segment implements an algorithm that includes at least two or more algorithms.  </p>
			<p>AND</p> 
			<p>• B.) At least one of the included algorithms uses mathematical or logical concepts. </p>
			<p>AND</p> 
			<p>• C.) Explains how one of the included algorithms functions independently.</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>A.) The selected code segment includes two algorithms (loginProcedure and createAccount procedures) that are integrated to create a new 
	             main algorithm (account access). </p>
			<p>AND</p>
			<p>B.) Both of the included procedures contain If/Else statements with Boolean conditions which count as logical concepts to satisfy the 
	             math/logic requirement.</p>
			<p>AND</p>
			<p>C.) The response explains how the loginProcedure procedure functions (“login in the user and load up the user’s diary entries if the 
	             correct password is entered. Otherwise, an error message will appear and the user will have to try again.”)</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>The statement “One of the integrated algorithms…” is a great way to call attention to the requirements for this part of the scoring criteria.  
	     When it comes to the logical/mathematical concepts, this response leaves a lot to the imagination and only states “ load up the user’s diary 
	     entries if the correct password is entered”.  By explicitly stating “My program uses logic to determine…”, one can take the guesswork out of 
	     awarding points for the grader.
	
	     This example does a nice job of explaining how both procedures do their work independently, but then also connects what they do in the 
	     conclusion.</p>
	<h4>Student Response</h4>
		<p>2c. As my program uses Firebase databases to store user data, AccountDB.GotValue is an important algorithm as it handles all data retrieved 
	         from the account database such as users and passwords. Because Firebase data requests are handled asynchronously to the program, it is 
	         necessary that when data is sent back from Firebase, the algorithm examines the tag and values sent back in order to properly redirect the 
	         program to either proceed with a login or create account procedure. 
		<br>One of the integrated algorithms is the procedure called loginProcedure (above). When called, the procedure loginProcedure will login in the 
	         user and load up the user’s diary entries if the correct password is entered. Otherwise, an error message will appear and the user will have to 
	         try again. 
		<br>The procedure createAccount shown above is another integrated algorithm that helps create a user’s account and mark the designated locations 
	         for the user’s data in Firebase given that they had provided a valid password and an unique username. The integration of the two procedures 
	         createAccount and loginProcedure helps the overall algorithm perform and regulate the core functions of the login screen of creating accounts 
	         and logging in.</p>
	</div>
	 
	<h3>Row 7: Applying Abstraction (Response 2D)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Selected code segment is a student-developed abstraction.</p>
			<p><i>Indicated by placing a rectangle around the specific piece of code in the entire program code section.</i></p> 
	         <p><i>If using the template, a screenshot is provided directly with the response.</i></p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>By the definition of abstraction, the selected code segment <i>does</i> implement an abstraction. The abstraction pictured here is a 
	             student-developed procedure called loadUserEntryData. </p>
			<p>The written response matches the selected code.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>The abstraction chosen is a procedure.  This is one of the easiest types of abstractions to develop and explain. </p>
	<h4>Student Response</h4>
	     <p><img src="../_static/assets/img/CreateSample12D.png" class="yui-img" title="" alt="">
	     </p>
		<p>2d. One abstraction I developed to manage the complexity of my code was the procedure loadUserEntryData. loadUserEntryData helps populate a 
	         list of user’s entries and is called multiple times throughout the program using different (albeit only slightly) parameters. Implementing this 
	         abstraction improves the readability of the code by reducing redundancy and the overall line count. Instead of repeating the nine lines of code 
	         in every place, I would only need to call the procedure loadUserEntryData. In addition, this abstraction manages complexity as any future 
	         changes that need to be made to loading user entry data can be done in a single place. Overall, this abstraction was a helpful in managing 
	         redundancy, length of code, editability, and overall complexity.</p>
	</div>
	
	<h3>Row 8: Applying Abstraction (Response 2D)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Explains how the selected abstraction manages the complexity of the program. </p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>The response indicates that the abstraction (procedure loadEntryData) “manages complexity as any future changes that need to be made to 
	             loading user entry data can be done in a single place. Overall, this abstraction was helpful in managing redundancy, length of code, edit 
	             ability, and overall complexity.”</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>This response is very well written.  It hits on several examples that would earn the point for the scoring criteria. One simple example is 
	     “Instead of repeating the nine lines of code in every place, I would only need to call the procedure loadUserEntryData.”</p>
	<h4>Student Response</h4>
		<p>2d. One abstraction I developed to manage the complexity of my code was the procedure loadUserEntryData. loadUserEntryData helps populate a 
	         list of user’s entries and is called multiple times throughout the program using different (albeit only slightly) parameters. Implementing this 
	         abstraction improves the readability of the code by reducing redundancy and the overall line count. Instead of repeating the nine lines of code 
	         in every place, I would only need to call the procedure loadUserEntryData. In addition, this abstraction manages complexity as any future 
	         changes that need to be made to loading user entry data can be done in a single place. Overall, this abstraction was a helpful in managing 
	         redundancy, length of code, editability, and overall complexity.</p>
	</div>
	     
	</div> <!-- accordion 1 -->
	
Sample 2 - 2018's Sample E
---------------------------

.. raw:: html

	   <div id="accordion2" class="yui-wk-div">
	
	<h3>Row 1: Developing a Program with a Purpose (Video and Response 2A)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) The video demonstrates the running of at least one feature of the program submitted. </p>
			<p>AND</p> 
			<p>B.) The response (audio narration or written response) identifies the purpose of the program 
			(what the program is attempting to do).</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>A.) The video is continuously running and illustrates the running of the program.</p>
			<p>AND</p>
			<p>B.) The response states the purpose as allowing the user to "put in whatever terms and definitions they desire and study off them later on 
	             flashcards."</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>While the video shows the running of the app, please be sure to take into consideration the atmosphere in which you record your video.  The 
	     background noise does not make the student lose points, but it does distract from the focus of the video.  The write up does a nice job of stating, 
	     “The purpose of the app…”</p>
	<h4>Student Response</h4>
		<a href="https://secure-media.collegeboard.org/ap/video_audio/ap18-create-sample-e-video.mp4" target="_blank" title="">Click here to watch 
	         video<br></a><p>2a.The program is a study guide app. The program was created in App Inventor 2. The purpose of this app is so that the user can 
	     put in whatever terms and definitions they desire and study off them later on flashcards. At first, the user puts in the desired term and 
	     definition in the two textboxes and then click submit allowing them to put in different terms and definitions after. When they are finally done, 
	     they click the study button which takes away the terms and definitions and just shows the term as a flashcard. Then to see what the definition is, 
	     they can click the flash card. The video shows the user plugging in values and later studying them as if there were real flashcards.</p>
	</div>
	
	<h3>Row 2: Developing a Program with a Purpose (Response 2B)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Describes or outlines steps used in the incremental and iterative development process to create the entire program.</p>
		</td>
		<td>
			<p>0</p>
		</td>
		<td>
			<p>The response does not describe the incremental or iterative process used in developing the entire program. The response focuses on two 
	             decisions that were made in determining what would be in the program. A good response would describe the steps taken to develop the program 
	             including information about the testing, debugging, and refinement of the program once the initial code was written.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>Focus on the process for this row of the scoring criteria.  The response to section 2b needs to cover both row 2 and row 3 on the scoring 
	     criteria. This response tries to cover row 3, but neglects to cover row 2. By keeping a journal of the process, a step-by-step description of 
	     the development of the app should be easy to put together for this requirement.</p>
	<h4>Student Response</h4>
		<p>2b. There were many problems that arose while coding the program. One of the early problems encountered was deciding how I should set up my 
	         study guide. For example, I could have chosen to do flashcards along with doing multiple choice. However, I felt that the flash cards would be 
	         more effective and efficient way of creating this app. Furthermore, when making this study guide app, I felt that there needed to be something 
	         else that could have made the study guide more useful for the reader. Originally, there were just flashcards, but I felt there was something 
	         else that could be done. So I included another button that allowed the user to type in the definition as the word was being given. This was a 
	         major development addition as it is more effective for the user to write the information than by just looking at cards. This is also more 
	         effective for memorization.</p>
	</div>
	
	<h3>Row 3: Developing a Program with a Purpose (Response 2B)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) Specifically identifies at least two program development difficulties or opportunities.  </p>
			<p>AND</p> 
			<p>B.) Describes how the two identified difficulties or opportunities are resolved or incorporated.</p>
		</td>
		<td>
			<p>0</p>
		</td>
		<td>
			<p>A.) The response only describes one program development difficulty/opportunity.</p>
			<p>AND</p>
			<p>B.) explains how that one difficulty/opportunity was resolved. </p>
			<p>The response identifies an opportunity as adding functionality to allow users to enter the "definition as the word was being given." This 
	             is resolved by including "another button."</p>
			<p>The difficulty identified is the decision to use flashcards over multiple choice, which is a design choice, not a program development 
	             difficulty.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>The lack of clarity in the response led this scorer to not award the point for this row.  “One of the early problems I encountered…” is the only 
	     part that stuck in the graders mind.  After describing that problem and its resolution, the student should have added the phrase, “Then I came 
	     across an opportunity to…”  This would have redirected the scorer’s attention to check off the requirements from the scoring criteria.</p>
	<h4>Student Response</h4>
		<p>2b. There were many problems that arose while coding the program. One of the early problems encountered was deciding how I should set up my 
	         study guide. For example, I could have chosen to do flashcards along with doing multiple choice. However, I felt that the flash cards would be 
	         more effective and efficient way of creating this app. Furthermore, when making this study guide app, I felt that there needed to be something 
	         else that could have made the study guide more useful for the reader. Originally, there were just flashcards, but I felt there was something 
	         else that could be done. So I included another button that allowed the user to type in the definition as the word was being given. This was a 
	         major development addition as it is more effective for the user to write the information than by just looking at cards. This is also more 
	         effective for memorization.</p>
	</div>
	   
	<h3>Row 4: Applying Algorithms (Response 2C)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Selected code segment implements an algorithm.</p>
			<p>Indicated by placing an oval around the specific piece of code in the entire program code section.</p> 
			<p>If using the template, a screenshot is provided directly with the response.</p>
	     	</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>By the definition of an algorithm, the selected code segment does implement an algorithm.<br> The main algorithm pictured here is the 
	             NextButton.Click block. <br>The written response matches the selected code.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>When selecting an algorithm, please be mindful of the definition.  It must be a formula or a set of steps in order to solve a problem.  Also be 
	     sure the selected algorithm will be sufficient to earn the points awarded for both row 5 and row 6.</p>
	<h4>Student Response</h4>
		<p>2c.&nbsp;<img src="../_static/assets/img/CreateSample22C.png" class="yui-img" title="" alt=""></p>
	</div>   
	   
	<h3>Row 5: Applying Algorithms (Response 2C)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) Selected code segment implements an algorithm that uses mathematical or logical concepts.</p>
			<p>AND</p> 
			<p>B.) Explains how the selected algorithm functions </p>
	         	<p>AND</p> 
	           <p>C.) Describes what the selected algorithm does in relation to the overall program.</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>A.) The selected code segment in this case is the main algorithm - the NextButton.click block. It satisfies the math/logic requirement 
	             because it uses an If/Else statement with Boolean conditions which counts as logic.</p>
			<p>AND</p>
			<p>B.)The response explains how the algorithm works: "When the next button is clicked, it displays the label font text and then doesn't show 
	             the back text. The index also determined which flashcard that you are on, in which you keep going to the next term as the next button is 
	             clicked. Furthermore, if the index is bigger than the number of items in the list then it restarts back to 1, or the first item in the 
	             list. This is the same for the other algorithm as they both use an index." </p>
			<p>AND</p>
	         	<p>C.) The response also describes what the purpose is for this algorithm in relation to the entire program: "allows the user to go to the 
	             next flashcard" and "the user has a study guide environment in which they can type in the necessary term to the definition and then be able 
	             to go to the next set of terms.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>To be sure to earn the point for row 5, students must clearly touch on all three of the “and” requirements.  The first is to assure that the 
	     algorithm uses mathematical or logical concepts.  The if/else block is used in this example meets that requirement.  The second part should follow 
	     with the step-by-step process of the algorithm.  This example doesn’t do a good job of that, but does enough to get the point across.  The last 
	     requirement is met as it relates the algorithm to the overall program in the introductory sentence.  This explicit type of technical writing leaves 
	     nothing up to interpretation.</p>
	<h4>Student Response</h4>
		<p>2c. This particular algorithm is essential to the program because it allows the user to go to the next flashcard. When the next button is 
	         clicked, it displays the label font text and then doesn't show the back text. The index also determined which flashcard that you are on, in 
	         which you keep going to the next term as the next button is clicked. Furthermore, if the index is bigger than the number of items in the list 
	         then it restarts back to 1, or the first item in the list. This is the same for the other algorithm as they both use an index. One of the 
	         independent algorithms makes so that user can type in the term as the other algorithm is displaying the definition as a flashcard. Together as 
	         a combination, this makes it so that the user has a study guide environment in which they can type in the necessary term to the definition and 
	         then be able to go to the next set of terms.</p>
	</div>
	   
	<h3>Row 6: Applying Algorithms (Response 2C)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>A.) Selected code segment implements an algorithm that includes at least two or more algorithms.  </p>
			<p>AND</p> 
			<p>B.) At least one of the included algorithms uses mathematical or logical concepts. </p>
			<p>AND</p> 
			<p>C.) Explains how one of the included algorithms functions independently.</p>
		</td>
		<td>
			<p>0</p>
		</td>
		<td>
			<p>A.) The selected code segment includes at least two algorithms that are integrated to create the main algorithm (NextButton). </p>
			<p>AND</p>
			<p>B.) The included algorithms all contain If/Else statements with Boolean conditions which count as logical concepts to satisfy the 
	             math/logic requirement.</p>
			<p>AND</p>
			<p>C.) The response briefly states that one algorithm "makes [it] so that user can type in the term as the other algorithm is displaying the 
	             definition as a flashcard." However, it is not clear where each of these algorithms is in the supplied code segment, so it is not clear if 
	             these algorithms are included in the identified algorithm.</p>
			<p><i>While the reader may be able to identify sub-algorithms in the main algorithm, the student’s response must clearly identify the sub-
	             algorithms and explain at least one sub-algorithm.</i></p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>Again, covering all three requirements is necessary to earn this point in the scoring criteria- 2 out of 3 did not get the job done on this 
	     example.  The two integrated algorithms from the overall algorithm are both if/else statements so that covers the first two requirements.  While 
	     the sentence starter “One of the independent algorithms…” is a great attention-getter for the reader, this example follows it up with an algorithm 
	     that is not part of the selected one.  Be sure students double-check their continuity to clean up this type of mistake.</p>
	<h4>Student Response</h4>
		<p>2c. This particular algorithm is essential to the program because it allows the user to go to the next flashcard. When the next button is clicked, it displays the label font text and then doesn't show the back text. The index also determined which flashcard that you are on, in which you keep going to the next term as the next button is clicked. Furthermore, if the index is bigger than the number of items in the list then it restarts back to 1, or the first item in the list. This is the same for the other algorithm as they both use an index. One of the independent algorithms makes so that user can type in the term as the other algorithm is displaying the definition as a flashcard. Together as a combination, this makes it so that the user has a study guide environment in which they can type in the necessary term to the definition and then be able to go to the next set of terms.</p>
	</div>
	   
	<h3>Row 7: Applying Abstraction (Response 2D)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Selected code segment is a student-developed abstraction.</p>
			<p><i>Indicated by placing a rectangle around the specific piece of code in the entire program code section.</i></p> 
			<p><i>If using the template, a screenshot is provided directly with the response.</i></p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>By the definition of abstraction, the selected code segment <i>does</i> implement an abstraction. The abstraction pictured here is a 
	             student-developed procedure called procedure. </p>
			<p>The written response matches the selected code.</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>The abstraction chosen is a procedure.  This is one of the easiest types of abstractions to develop and explain.</p>
	<h4>Student Response</h4>
		<p>2d.&nbsp;<img src="../_static/assets/img/CreateSample22D.png" class="yui-img" title="" alt=""></p>
	</div>
	   
	<h3>Row 8: Applying Abstraction (Response 2D)</h3>
	<div class="yui-wk-div">
	<table>
	<tbody><tr>
		<th>Requirements</th>
		<th>Score</th>
		<th>Explanation</th>
	</tr>
	<tr>
		<td>
			<p>Explains how the selected abstraction manages the complexity of the program.</p>
		</td>
		<td>
			<p>1</p>
		</td>
		<td>
			<p>The response gives a reason why the abstraction (procedure) manages complexity: "By creating this abstraction it makes the general coding 
	             clearer and easier to read as it is already being used once."</p>
		</td>
	</tr>
	</tbody></table>
	<h4>Additional Explanation</h4>
	<p>While this explanation does a good job of telling what the procedure does, it waits until the last sentence to earn the point.  Giving the reader 
	     the reasons  “...makes the general coding clearer and easier to read…” effectively illustrates the managing of the complexity.  It also subtly 
	     points out how it reduces redundancy.</p>
	<h4>Student Response</h4>
		<p>2d. This particular abstraction is used to determine if the word you type in, is correct. This abstraction uses mathematical concepts by 
	         determining if the word you type in and the actual term, are equal. If they do happen to be equal, then this will be shown in the 
	         “lblWriteWrong.” Furthermore, this abstraction uses logical concepts by determining if the word the user types in is true, then it will be 
	         displayed as correct through the Write Wrong label. However if the word the user types in is a false word, then it will show that it is 
	         incorrect through the Write Wrong label. By creating this abstraction it makes the general coding clearer and easier to read as it is already 
	         being used once. </p>
	</div>
	</div> <!-- accordion 2-->	

