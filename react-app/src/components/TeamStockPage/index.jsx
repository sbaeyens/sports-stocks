import React, { useEffect } from 'react'
import { useDispatch, useSelector } from "react-redux";
import { fetchTeamHistory, clearTeamsOddsState } from '../../store/oddsHistory';

function TeamStockPage() {
    const dispatch = useDispatch()
    const oddsHistory = useSelector((state) => state.oddsHistory?.team);

    console.log("oddsHistory", oddsHistory);

    let oddsHistoryArray = Object.values(oddsHistory)
    console.log("oddsHistoryArray", oddsHistoryArray);

    useEffect(() => {
        dispatch(fetchTeamHistory("NBA", "DEN"))

        return () => {
          dispatch(clearTeamsOddsState());
        };

    }, [dispatch])


  return (
    <div>TeamStockPage</div>
  )
}

export default TeamStockPage
