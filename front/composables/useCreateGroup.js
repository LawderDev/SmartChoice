import axios from 'axios';

export function useCreateGroup() {
    const stateCreateGroup = reactive({
      group: [],
    })
    
    const getAllGroups = async () => {
        try {
          const data = {
            sessionID: route.params.sessionId
          }
    
          const jsonData = JSON.stringify(data);
    
          const res = await axios.post(
            "http://127.0.0.1:5000/api/get_all_groups_students",
            jsonData,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          );
          
          state.groups = res.data
        } catch (err) {
          console.error(err);
        }
      }

      return {
          stateCreateGroup,
          getAllGroups,
      }
}