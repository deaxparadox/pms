
import { Task } from "./config.service"

// {
//     "id": 1,
//     "created": "2023-10-07T14:49:27.015000Z",
//     "updated": "2023-10-07T14:49:27.015000Z",
//     "heading": "October",
//     "start": null,
//     "end": null
// },

export interface Heading {
    id: number
    heading: string,
    created: string,
    updated: string,
    start: string | null,
    end: string | null
}


// {
//     "id": 1,
//     "heading": "October",
//     "start": null,
//     "end": null,
//     "created": "2023-10-07T14:49:27.015000Z",
//     "updated": "2023-10-07T14:49:27.015000Z",
//     "tasks": [
//         {
//             "task": "c binary tree",
//             "start": "2023-10-01",
//             "end": "2023-10-31",
//             "created": "2023-10-07T16:11:00.375000Z",
//             "updated": "2023-10-07T16:36:42.827000Z"
//         }
//     ]
// },

export interface HeadingWithTasks {
    id: number,
    heading: string,
    start: string | null,
    end: string | null,
    created: string,
    updated: string,
    tasks: Task[]
}