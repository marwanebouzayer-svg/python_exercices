const people = ["Greg", "Mary", "Devon", "James"];

people.splice(0, 1);
people[2] = "Jason";
people.push("Marwane");

console.log(people.indexOf("Mary"));

const newPeople = people.slice(1, 3);
console.log(newPeople);

console.log(people.indexOf("Foo"));

const last = people[people.length - 1];
console.log(last);

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
        break;
    }
}