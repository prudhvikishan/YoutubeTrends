
<?php
	
	$command = escapeshellcmd('python topchannels.py');
	$output = json_decode(exec($command), true);
	$command2 = escapeshellcmd('python topchannels.py a');
	$output2 = json_decode(exec($command2), true);
	$outputStr = "<div><table style = \"width: 100%\">";
	$outputStr .= "<tr><td><h3>Channel</h3></td><td><h3>Combined Engagement Score</h3></td></tr>";
	for($i = 0; $i < 10; $i++)
	{
		$outputStr .= "<tr><td>" . $output[$i][0] . " </td><td>" . $output2[$i][0] .  "</td></tr>";
	}
	$outputStr .= "</div>";

	echo($outputStr);
?>