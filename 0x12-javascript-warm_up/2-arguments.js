const a = process.argv.slice(2);

if (a.length === 0) {
    console.log("No argument");
} else if (a.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}

