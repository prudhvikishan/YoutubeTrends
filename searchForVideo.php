
<?php
	$query = $_GET["q"];
	
	$command = 'python searchforvideo.py ' . $query;
	$output = json_decode(exec($command), true);
	$max = $output[0];
	$outputStr = "<div><table style = \"width: 100%\">";
	$outputStr .= "<tr><td><h3>Video Title</h3></td><td><h3>ID Number</h3></td></tr>";
	for($i = 1; $i <= $max; $i++)
	{
			$outputStr .= "<tr><td>" . $output[$i][0] . "</td><td> " . $output[$i][1] . "</td></tr>";
	}
	$outputStr .= "</table></div>";
	
	echo $outputStr;
?>