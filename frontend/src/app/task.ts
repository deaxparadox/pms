// {
//     "id": 1,
//     "created": "2023-10-07T15:32:12.935000Z",
//     "updated": "2023-10-07T16:54:32.056000Z",
//     "task": "c learn",
//     "start": "2023-10-02",
//     "end": "2023-10-15",
//     "heading": 3
// },

export interface Task {
    id: number,
    created: string,
    updated: string,
    task: string,
    start: string,
    end: string,
    heading: number
}