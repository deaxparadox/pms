import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Heading, HeadingWithTasks } from './heading';

@Injectable({
  providedIn: 'root'
})
export class HeadingService {

  constructor(private httpClient: HttpClient) { }

  getHeadings(): Observable<Heading[]> {
    return this.httpClient.get<Heading[]>("http://localhost:8000/api/v1/")
  }
  getHeading(id: number): Observable<HeadingWithTasks> {
    return this.httpClient.get<HeadingWithTasks>(`http://localhost:8000/api/v1/heading/${id}/`)
  }
}
