import React, { useEffect } from 'react'
import { useDispatch, useSelector } from "react-redux";
import { fetchTeamHistory, clearTeamsOddsState } from '../../store/oddsHistory';
import TeamStockChart from '../TeamStockChart';

function TeamStockPage() {
    const dispatch = useDispatch()
    const oddsHistory = useSelector((state) => state.oddsHistory?.team);

    console.log("oddsHistory", oddsHistory);



    useEffect(() => {
        dispatch(fetchTeamHistory("NBA", "DEN"))

        return () => {
          dispatch(clearTeamsOddsState());
        };

    }, [dispatch])


  return (
      <div>
          <div className="chart">
              <TeamStockChart oddsHistory = {oddsHistory} />
          </div>
    </div>
  )
}

export default TeamStockPage
