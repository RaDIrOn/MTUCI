var groupmates = [
    {
        "name": "Максим",
        "group": "2254",
        "age": 25,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "2254",
        "age": 24,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Вадим",
        "group": "2254",
        "age": 24,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Вика",
        "group": "2254",
        "age": 23,
        "marks": [5, 5, 5, 4, 5]
    }
];

function rpad(str, length) {
    str = str.toString();
    while (str.length < length) {
        str = str + ' ';
    }
    return str;
}

function printStudents(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
    
    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
}

console.log("Список студентов:");
printStudents(groupmates);

function filterByGroup(students, group) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'] === group) {
            filtered.push(students[i]);
        }
    }
    return filtered;
}

console.log("Студенты группы 2254:");
var group912_1 = filterByGroup(groupmates, "2254");
printStudents(group912_1);