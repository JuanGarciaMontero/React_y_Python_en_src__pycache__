import React from 'react';
import { Task } from '../../models/task.class';
//import { LEVELS } from '../../models/task.enum';
import TaskComponent from '../pure/task';
import PropTypes from 'prop-types';

const TaskListComponent = (props) => {

    //const defaultTask = new Task('Example', 'Default description', false, LEVELS.NORMAL);
    
    let conex='false';
    if (props.nombre ===''|| props.apellido ==='' || props.email ===''){conex='false'} else {conex='true'};
    const defaultTask = new Task('', '', '', conex);
    /*changeState = (id) => {
        console.log('TODO: Cambiar estado de una tarea')
    }*/

    return (
        <div>
            <div>
                <h1>
                    Tus datos:
                </h1>
                <h2>
                    Nombre: { props.nombre }
                </h2>
                <h2>
                    Apellidos: {  props.apellido }
                </h2>
                <h3>
                    Email: {  props.email}
                </h3>
            </div>
            {/* TODO: Aplicar un For/Map para renderizar una lista */}
            <TaskComponent task={defaultTask}></TaskComponent>
        </div>
    );
};

TaskListComponent.propTypes = {
    name: PropTypes.string,
    apellido: PropTypes.string,
    email: PropTypes.string
};


export default TaskListComponent;
