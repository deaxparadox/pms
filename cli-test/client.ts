let headers = new Headers();
headers.append('Access-Control-Allow-Origin', '*');
headers.append('Access-Control-Allow-Headers', 'Content-Type');
headers.append('Content-Type', 'application/json')

const f = await fetch("http://localhost:8000/api/v1/", {
    headers: headers,
    keepalive: true
});
console.log(await f.json());
console.log(await f.headers)