import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs';

export interface Task {
  created: string;
  updated: string;
  task: string;
  heading: number;
  start: string | null;
  end: string | null
}

@Injectable({
  providedIn: 'root'
})
export class ConfigService {
  taskUrl = "http://localhost:8000/api/v1/task/"

  constructor(private http: HttpClient) { }

  getTask() {
    return this.http.get<Task>(this.taskUrl);
  }

}
