from flask_restful import Resource, request
from models.npc import Npc

class NpcDialogue(Resource):
    def get(self):
        npc_id = request.args.get('npc_id')
        try:
            if npc_id:
                npc = Npc.query.get(npc_id)
                if not npc:
                    return {"error": "NPC not found."}, 404
                return {"npc_id": npc_id, "dialogue": npc.dialogue}, 200
            else:
                all_npcs = [{"npc_id": npc.id, "dialogue": npc.dialogue} for npc in Npc.query.all()]
                return all_npcs, 200
        except Exception as e:
            return {"error": str(e)}, 400
