import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Task } from '../../config.service';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  constructor(public httpClient: HttpClient) { }

  getTasks(): Observable<Task[]> {
    return this.httpClient.get<Task[]>("http://localhost:8000/api/v1/task/")
  }
}
