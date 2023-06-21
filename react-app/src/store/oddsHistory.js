// Actions ----------------------------------------------------------------------
export const GET_TEAM_HISTORY = "history/GET_TEAM_HISTORY";
export const CLEAR_TEAM_HISTORY_STATE = "history/CLEAR_TEAM_HISTORY_STATE";

// Action creators --------------------------------------------------------------

export const clearTeamsOddsState = () => {
  return {
    type: CLEAR_TEAM_HISTORY_STATE,
  };
};

export const getTeamOddsHistory = (payload) => {
  return {
    type: GET_TEAM_HISTORY,
    payload,
  };
};

// Thunk functions --------------------------------------------------------------
export const fetchTeamHistory = (league, code) => async (dispatch) => {
  const response = await fetch(`/api/odds_history/${league}/${code}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(getTeamOddsHistory(data));
    return;
  }
};


const initialState = { team: null };

export default function oddsHistoryReducer(state = initialState, action) {
  let newState = { ...state };
  switch (action.type) {
    case GET_TEAM_HISTORY:
      let historyList = {};
      action.payload.forEach((history) => {
        historyList[history.id] = history;
      });
      newState.team = { ...historyList };
      return newState;

    case CLEAR_TEAM_HISTORY_STATE:
      return { ...initialState };

    default:
      return state;
  }
}
