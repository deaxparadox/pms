import { Component, OnInit } from '@angular/core';
import { Task } from 'src/app/config.service';
import { TaskService } from 'src/app/services/task/task.service';


@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit{
  constructor(
    private httpClientTask: TaskService
  ) {}

  ngOnInit(): void {
    this.getTasks();
  }
  tasks?: Task[];

  getTasks() {
    this.httpClientTask.getTasks().subscribe(
      tasks => {
        this.tasks = tasks;
      }
    )

  }


}
