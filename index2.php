<!DOCTYPE html>
<!--
Colors Used:
Almost Black: #282828
Dark Gray: #303030
Red: #FF0000
White: #FFFFFF
-->
<html lang = "en-us">
	<head>
		<meta charset = "UTF-8">
		<meta name = "decription" content = "YouTube analytics">
		<meta name = "authors" content = "Andrew Murphy, Prudhvi Kishan Kotamarthy, Harvey Petersen">
		<meta name = "viewport" content = "width = device - width, initial-scale = 1.0">
		
		<title>YouTrends</title>
		
		<style>
			html
			{
				margin: 0px, 50px;
				padding: 0;
				background: #FF0000;
				font-family: Verdana, sans serif;
			}
			
			body
			{
				margin: 0;
				padding: 0;
				background: #FFFFFF;
			}
			
			.pageHeader
			{
				margin: 0px;
				background: #FF0000;
				color: #FFFFFF;
			}
			
			h1
			{
				text-align: center;
				font-size: 30px;
				margin: 5px 50px 0px;
			}
			
			h2
			{
				text-align: center;
				font-size: 25px;
				margin: 5px 50px 0px;
			}
			
			p
			{
				background: #FFFFFF;
				margin: 5px 150px;
				text-align: center;
			}
			
			hr
			{
				margin: 0px;
			}
			
			form
			{
				text-align: center;
			}
		</style>
	
	</head>

	<body onload = "pageLoad()"> 
		<section class = "pageHeader"> <!-- Page Headder -->
			<h1> YouTrends </h1>
		</section>
		<hr>
		<section> <!-- Intro Paragraph -->
			<p>
				Hello! <br>
				Welcome to YouTrends, an analytics tool for YouTube! We are <b>not</b> affiliated with Youtube in any way. <br>
				This is designed for content creators on the YouTube platform (and for those who are interested in the numbers). <br>
				This program gathers information about the top 1,000 videos on a regular basis and does analysis on the data. <br>
			</p>
		</section>
		<hr>
		<section> <!-- Top 10 Videos -->
			<h2>
				Top 10 Videos:
			</h2>
			<p id = "top10Vid">
				<?php
				$command = escapeshellcmd('python topvideos.py');
				$output = exec($command);
				
				print($output);
				?>
			</p>
		</section>
		<hr>
		<section> <!-- Top 10 Channels -->
			<h2>
				Top 10 Channels:
			</h2>
			<p id = "top10Chan">
				<?php
				$command = escapeshellcmd('python topchannels.py');
				$output = exec($command);
				
				print($output);
				?>
			</p>
		</section>
		<hr>
		<section> <!-- Explain Engagement -->
			<h2>
				How do we determine top videos and channels?:
			</h2>
			<p>
				You might be thinking, 'how does the website know which is best?' Well, we use a value called engagement score! For each video, we consider the number of views, comments, and likes/dislikes to equate that video's score. For every channel, we analyze the videos from that channel that have made it to the top 1,000 (if any) and combine those videos's scores together to generate the channel's score.
				
				
				
			</p>
		</section>
		<hr>
		<section> <!-- Search a Video! -->
			<h2>
				Search a Video!:
			</h2>
			<form>
				<input id = "searchVid" type = "text" style = "width: 300px;" placeholder = "Video Name" \>
				<input id = "goButton" type = "button" value = "Enter" onclick = "findVideo()" \>
			</form>
		</section>
		
		<section> <!-- Javascript to access PHP and client-side formatting -->
			<script>
				function pageLoad()
				{
					getTopChannels();
					getTopVideos();
				}
				
				function getTopChannels()
				{
					
				}
				
				function getTopVideos()
				{
				
				}
				
				
				
				function toPHP(dest, output)
				{
					var xmlhttp = new XMLHttpRequest();
					xmlhttp.onreadystatechange = function()
					{
						if(this.readyState == 4 && this.status == 200)
						{
							document.getElementById(dest).innerHTML = this.responseText;
						}
					}
					xmlhttp.open("GET", dest, true);
					xmlhttp.send();
				}
			</script>
		</section>
	</body>

</html>
