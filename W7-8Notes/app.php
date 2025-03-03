<?php
$version = getenv("VERSION");
$backgroundColor = ($version === "v1.0.0") ? "skyblue" : "green";
$message = NULL;
if ($backgroundColor == "green") {
    $message = "This is the new version: $version";
} else {
    $message = "This is the old version: $version";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP and HTML Example</title>
    <style>
        body {
            background-color: <?php echo $backgroundColor; ?>;
        }
    </style>
</head>
<body>
    <h1> <?php echo $message; ?> </h1>
</body>
</html>