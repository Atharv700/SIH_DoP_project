<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sustainability Tracker</title>
</head>
<body>
    <h1>Sustainability Tracker</h1>
    <form action="/submit" method="post">
        <label for="energy">Energy Consumed (kWh):</label>
        <input type="number" name="energy" required><br><br>

        <label for="waste">Waste Generated (kg):</label>
        <input type="number" name="waste" required><br><br>

        <label for="water">Water Used (liters):</label>
        <input type="number" name="water" required><br><br>

        <label for="comments">Comments:</label>
        <textarea name="comments" required></textarea><br><br>

        <button type="submit">Submit Report</button>
    </form>
</body>
</html>
