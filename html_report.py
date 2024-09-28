<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
</head>
<body>
    <h1>Reports Summary</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Energy Consumed (kWh)</th>
            <th>Waste Generated (kg)</th>
            <th>Water Used (liters)</th>
            <th>Comments</th>
        </tr>
        {% for row in data %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
