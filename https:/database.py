c.execute("INSERT INTO badges (user_id,badge_name,earned_date) VALUES (?,?,?)",
                      (user_id, badge_name, str(date.today())))
            self.conn.commit()
            return True
        return False

    def get_badges(self, user_id):
        c = self.conn.cursor()
        c.execute("SELECT badge_name FROM badges WHERE user_id=?", (user_id,))
        return c.fetchall()

    def get_leaderboard(self, limit=10):
        c = self.conn.cursor()
        c.execute("SELECT name,xp,level,streak FROM users ORDER BY xp DESC LIMIT ?", (limit,))
        return c.fetchall()

    def save_mooc_result(self, user_id, subject, score, total):
        week = datetime.now().strftime("%Y-W%U")
        ratio = score/total if total>0 else 0
        level = "🥇 Oltin" if ratio>=0.9 else "🥈 Kumush" if ratio>=0.7 else "🥉 Bronza"
        self.conn.execute("INSERT INTO mooc_results (user_id,week,subject,score,total,certificate_level,date) VALUES (?,?,?,?,?,?,?)",
                          (user_id, week, subject, score, total, level, str(date.today())))
        self.conn.commit()
        return level
